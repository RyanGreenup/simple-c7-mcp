# Altinity Kubernetes Operator for ClickHouse

The Altinity Kubernetes Operator for ClickHouse is a Go-based Kubernetes operator that automates the deployment, configuration, and lifecycle management of ClickHouse database clusters on Kubernetes. It implements the operator pattern using custom resource definitions (CRDs) to provide declarative management of ClickHouse installations. The operator handles complex operations including cluster creation, scaling, version upgrades, schema propagation, user management, and persistent storage provisioning while exposing Prometheus metrics for monitoring.

Built with the Kubernetes client-go library and controller-runtime framework, the operator watches for ClickHouseInstallation custom resources and reconciles the desired state with actual cluster state. It manages StatefulSets, Services, ConfigMaps, and PersistentVolumeClaims to create production-ready ClickHouse clusters with features like replication, sharding, custom pod templates, and ZooKeeper/ClickHouse Keeper integration for distributed coordination. The project includes a separate metrics exporter component for gathering ClickHouse-specific telemetry and integrates with standard Kubernetes RBAC for security.

## APIs and Key Functions

### Install ClickHouse Operator

Deploy the operator to Kubernetes cluster using kubectl with the installation manifest.

```bash
# Install operator in kube-system namespace (watches all namespaces)
kubectl apply -f https://raw.githubusercontent.com/Altinity/clickhouse-operator/master/deploy/operator/clickhouse-operator-install-bundle.yaml

# Or install in custom namespace using installer script
curl -s https://raw.githubusercontent.com/Altinity/clickhouse-operator/master/deploy/operator-web-installer/clickhouse-operator-install.sh | OPERATOR_NAMESPACE=clickhouse-system bash

# Verify operator is running
kubectl get pods -n clickhouse-system
# Expected output:
# NAME                                   READY   STATUS    RESTARTS   AGE
# clickhouse-operator-5ddc6d858f-drppt   1/1     Running   0          1m

# Check operator logs
kubectl logs -n clickhouse-system deployment/clickhouse-operator
```

### Create Simple ClickHouse Cluster

Define a ClickHouseInstallation custom resource with basic configuration for a single-node cluster.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "simple-01"
  namespace: "default"
spec:
  configuration:
    users:
      # SHA256 hash of 'test_password'
      test_user/password_sha256_hex: 10a6e6cc8311a3e2bcc09bf6c199adecd5dd59408c343e926b129c4914f3cb01
      test_user/password: test_password
      test_user/networks/ip:
        - 0.0.0.0/0
    clusters:
      - name: "simple"
```

```bash
# Apply the manifest
kubectl apply -f simple-cluster.yaml

# Wait for cluster to be ready
kubectl get chi simple-01 -w

# Get pod name
kubectl get pods -l clickhouse.altinity.com/chi=simple-01

# Connect to ClickHouse
kubectl exec -it chi-simple-01-simple-0-0-0 -- clickhouse-client -u test_user --password test_password
```

### Create Replicated ClickHouse Cluster with Persistent Storage

Configure a production cluster with multiple shards, replicas, and persistent volumes.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "production-cluster"
spec:
  defaults:
    templates:
      podTemplate: clickhouse-production
      dataVolumeClaimTemplate: data-volume
      logVolumeClaimTemplate: log-volume
  configuration:
    zookeeper:
      nodes:
        - host: zookeeper-0.zookeeper-headless.default.svc.cluster.local
          port: 2181
        - host: zookeeper-1.zookeeper-headless.default.svc.cluster.local
          port: 2181
        - host: zookeeper-2.zookeeper-headless.default.svc.cluster.local
          port: 2181
    clusters:
      - name: "prod"
        layout:
          shardsCount: 3
          replicasCount: 2
  templates:
    podTemplates:
      - name: clickhouse-production
        spec:
          containers:
            - name: clickhouse
              image: clickhouse/clickhouse-server:24.8
              resources:
                requests:
                  memory: "4Gi"
                  cpu: "2"
                limits:
                  memory: "8Gi"
                  cpu: "4"
    volumeClaimTemplates:
      - name: data-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 100Gi
          storageClassName: gp3
      - name: log-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 10Gi
```

```bash
# Apply configuration
kubectl apply -f production-cluster.yaml

# Monitor deployment progress
kubectl get chi production-cluster -o jsonpath='{.status.status}' -w

# List all pods (should see 6 pods: 3 shards × 2 replicas)
kubectl get pods -l clickhouse.altinity.com/chi=production-cluster

# Get service endpoints
kubectl get svc -l clickhouse.altinity.com/chi=production-cluster
```

### Configure ClickHouse Users and Access Control

Define users with passwords, network restrictions, profiles, and quotas.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: clickhouse-credentials
type: Opaque
stringData:
  admin_password: "supersecret123"
  readonly_password_sha256: "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5"
---
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "secure-cluster"
spec:
  configuration:
    users:
      # Admin user with secret reference
      admin/k8s_secret_password: clickhouse-credentials/admin_password
      admin/networks/ip:
        - "10.0.0.0/8"
        - "192.168.0.0/16"
      admin/profile: admin_profile
      admin/quota: default

      # Readonly user with SHA256 hash
      readonly/k8s_secret_password_sha256_hex: clickhouse-credentials/readonly_password_sha256
      readonly/profile: readonly
      readonly/quota: default

      # Application user with grants
      app_user/password: app_password_123
      app_user/allow_databases/database:
        - "analytics"
        - "logs"

    profiles:
      admin_profile/max_memory_usage: 10000000000
      admin_profile/max_execution_time: 0
      readonly/readonly: 1
      readonly/max_execution_time: 300

    quotas:
      default/interval/duration: 3600
      default/interval/queries: 1000
      default/interval/errors: 100

    clusters:
      - name: "secure"
        layout:
          shardsCount: 1
          replicasCount: 1
```

```bash
# Apply configuration
kubectl apply -f secure-cluster.yaml

# Test connection with admin user
kubectl exec -it chi-secure-cluster-secure-0-0-0 -- \
  clickhouse-client -u admin --password supersecret123 --query "SELECT currentUser()"

# Test readonly user restrictions
kubectl exec -it chi-secure-cluster-secure-0-0-0 -- \
  clickhouse-client -u readonly --query "CREATE TABLE test (id Int32) ENGINE=Memory"
# Expected: Code: 164. DB::Exception: readonly: Cannot execute query in readonly mode
```

### Configure Custom ClickHouse Settings and Files

Inject custom configuration files and settings into ClickHouse instances.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "custom-config"
spec:
  configuration:
    settings:
      # Compression settings
      compression/case/method: zstd
      compression/case/min_part_size: 10000000
      compression/case/min_part_size_ratio: 0.01

      # Performance settings
      max_concurrent_queries: 100
      max_table_size_to_drop: 0
      disable_internal_dns_cache: 1

    files:
      # External dictionary definition
      dictionaries.xml: |
        <dictionaries>
          <dictionary>
            <name>geo_dictionary</name>
            <source>
              <file>
                <path>/var/lib/clickhouse/user_files/geo_data.csv</path>
                <format>CSV</format>
              </file>
            </source>
            <layout>
              <hashed />
            </layout>
            <structure>
              <id>
                <name>id</name>
              </id>
              <attribute>
                <name>country</name>
                <type>String</type>
              </attribute>
            </structure>
            <lifetime>3600</lifetime>
          </dictionary>
        </dictionaries>

      # Custom macros
      macros.xml: |
        <macros>
          <environment>production</environment>
          <datacenter>us-east-1</datacenter>
        </macros>

    clusters:
      - name: "configured"
        layout:
          shardsCount: 1
          replicasCount: 1
```

```bash
# Apply custom configuration
kubectl apply -f custom-config.yaml

# Verify settings applied
kubectl exec -it chi-custom-config-configured-0-0-0 -- \
  clickhouse-client --query "SELECT name, value FROM system.settings WHERE name LIKE '%concurrent%'"

# Check loaded dictionaries
kubectl exec -it chi-custom-config-configured-0-0-0 -- \
  clickhouse-client --query "SELECT name, status FROM system.dictionaries"

# View applied macros
kubectl exec -it chi-custom-config-configured-0-0-0 -- \
  clickhouse-client --query "SELECT * FROM system.macros"
```

### Scale ClickHouse Cluster

Modify cluster layout to add or remove shards and replicas with automatic schema propagation.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "scalable-cluster"
spec:
  configuration:
    zookeeper:
      nodes:
        - host: zookeeper.default.svc.cluster.local
          port: 2181
    clusters:
      - name: "scaling"
        layout:
          shardsCount: 5  # Increased from 3
          replicasCount: 3  # Increased from 2
  templates:
    volumeClaimTemplates:
      - name: data-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 50Gi
```

```bash
# Get current cluster topology
kubectl get chi scalable-cluster -o jsonpath='{.status.clusters[0].shardsCount},{.status.clusters[0].replicasCount}'

# Apply scaled configuration
kubectl apply -f scalable-cluster.yaml

# Monitor scaling progress
kubectl get pods -l clickhouse.altinity.com/chi=scalable-cluster -w

# Verify new pods are running (should see 15 pods: 5 shards × 3 replicas)
kubectl get pods -l clickhouse.altinity.com/chi=scalable-cluster --show-labels

# Check cluster configuration from ClickHouse
kubectl exec -it chi-scalable-cluster-scaling-0-0-0 -- \
  clickhouse-client --query "SELECT cluster, shard_num, replica_num, host_name FROM system.clusters WHERE cluster='scaling' ORDER BY shard_num, replica_num"
```

### Upgrade ClickHouse Version

Update ClickHouse version across cluster with rolling update strategy.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "version-upgrade"
spec:
  configuration:
    clusters:
      - name: "upgrade"
        layout:
          shardsCount: 2
          replicasCount: 2
  templates:
    podTemplates:
      - name: clickhouse-v24-8
        spec:
          containers:
            - name: clickhouse
              image: clickhouse/clickhouse-server:24.8  # Upgraded from 24.3
              imagePullPolicy: IfNotPresent
    volumeClaimTemplates:
      - name: data-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 20Gi
  defaults:
    templates:
      podTemplate: clickhouse-v24-8
      dataVolumeClaimTemplate: data-volume
```

```bash
# Check current versions
kubectl get pods -l clickhouse.altinity.com/chi=version-upgrade -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[0].image}{"\n"}{end}'

# Apply version upgrade
kubectl apply -f version-upgrade.yaml

# Watch rolling update
kubectl rollout status statefulset/chi-version-upgrade-upgrade-0-0
kubectl rollout status statefulset/chi-version-upgrade-upgrade-0-1

# Verify new version running
kubectl exec -it chi-version-upgrade-upgrade-0-0-0 -- clickhouse-client --query "SELECT version()"
```

### Deploy with Custom Pod Templates and Resources

Define custom pod specifications with resource limits, node affinity, and tolerations.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "custom-pods"
spec:
  configuration:
    clusters:
      - name: "custom"
        templates:
          podTemplate: clickhouse-custom
        layout:
          shardsCount: 2
          replicasCount: 2
  templates:
    podTemplates:
      - name: clickhouse-custom
        spec:
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                - labelSelector:
                    matchExpressions:
                      - key: clickhouse.altinity.com/chi
                        operator: In
                        values:
                          - custom-pods
                  topologyKey: kubernetes.io/hostname
          tolerations:
            - key: "clickhouse"
              operator: "Equal"
              value: "true"
              effect: "NoSchedule"
          containers:
            - name: clickhouse
              image: clickhouse/clickhouse-server:24.8
              resources:
                requests:
                  memory: "8Gi"
                  cpu: "4"
                limits:
                  memory: "16Gi"
                  cpu: "8"
              env:
                - name: TZ
                  value: "America/New_York"
              volumeMounts:
                - name: data-volume
                  mountPath: /var/lib/clickhouse
                - name: log-volume
                  mountPath: /var/log/clickhouse-server
    volumeClaimTemplates:
      - name: data-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 200Gi
          storageClassName: fast-ssd
      - name: log-volume
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 20Gi
```

```bash
# Apply custom pod template
kubectl apply -f custom-pods.yaml

# Verify pod placement (should be on different nodes due to anti-affinity)
kubectl get pods -l clickhouse.altinity.com/chi=custom-pods -o wide

# Check resource allocations
kubectl describe pod chi-custom-pods-custom-0-0-0 | grep -A5 "Limits:\|Requests:"

# Verify tolerations applied
kubectl get pod chi-custom-pods-custom-0-0-0 -o jsonpath='{.spec.tolerations}'
```

### Setup Monitoring with Prometheus

Configure metrics endpoint and ServiceMonitor for Prometheus scraping.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseInstallation"
metadata:
  name: "monitored-cluster"
spec:
  configuration:
    clusters:
      - name: "monitored"
        layout:
          shardsCount: 2
          replicasCount: 1
  defaults:
    templates:
      serviceTemplate: chi-service-with-metrics
  templates:
    serviceTemplates:
      - name: chi-service-with-metrics
        spec:
          ports:
            - name: http
              port: 8123
            - name: tcp
              port: 9000
            - name: metrics
              port: 9363
          type: ClusterIP
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: clickhouse-metrics
  labels:
    app: clickhouse
spec:
  selector:
    matchLabels:
      clickhouse.altinity.com/chi: monitored-cluster
  endpoints:
    - port: metrics
      interval: 30s
      path: /metrics
---
apiVersion: v1
kind: Service
metadata:
  name: clickhouse-operator-metrics
  labels:
    app: clickhouse-operator
spec:
  ports:
    - name: metrics
      port: 8888
      targetPort: 8888
  selector:
    app: clickhouse-operator
```

```bash
# Apply monitoring configuration
kubectl apply -f monitored-cluster.yaml

# Check metrics endpoint is accessible
kubectl port-forward svc/chi-monitored-cluster-monitored-0-0 9363:9363 &
curl -s http://localhost:9363/metrics | grep clickhouse_

# Verify ServiceMonitor created
kubectl get servicemonitor clickhouse-metrics

# Query Prometheus for ClickHouse metrics (if Prometheus installed)
kubectl port-forward -n monitoring svc/prometheus-k8s 9090:9090 &
# Open browser to http://localhost:9090 and query: clickhouse_metric_Query
```

### Configure Operator Settings

Customize operator behavior through ClickHouseOperatorConfiguration resource.

```yaml
apiVersion: "clickhouse.altinity.com/v1"
kind: "ClickHouseOperatorConfiguration"
metadata:
  name: clickhouse-operator-config
  namespace: clickhouse-system
spec:
  watch:
    namespaces:
      - "production"
      - "staging"

  clickhouse:
    configuration:
      user:
        default:
          profile: "default"
          quota: "default"
          networksIP:
            - "::1"
            - "127.0.0.1"
            - "10.0.0.0/8"
          password: "default"
      network:
        hostRegexpTemplate: "^chi-{chi}-[^.]+\\d+-\\d+\\.{namespace}\\.svc\\.cluster\\.local$"

    access:
      scheme: "http"
      username: "clickhouse_operator"
      password: "clickhouse_operator_password"
      rootCA: ""
      port: 8123

  template:
    chi:
      replicasUseFQDN: "yes"

  reconcile:
    runtime:
      threadsNumber: 10

    statefulSet:
      create:
        onFailure: "abort"
      update:
        timeout: 300
        pollInterval: 5
        onFailure: "rollback"

  annotation:
    include:
      - "custom.annotation/*"
    exclude:
      - "exclude.this.annotation"

  label:
    include:
      - "custom.label/*"
    exclude: []
```

```bash
# Apply operator configuration
kubectl apply -f operator-config.yaml

# Restart operator to apply new configuration
kubectl rollout restart deployment/clickhouse-operator -n clickhouse-system

# Verify configuration loaded
kubectl logs -n clickhouse-system deployment/clickhouse-operator | grep -i "configuration"

# Check operator watches correct namespaces
kubectl get chi --all-namespaces
```

### Run Metrics Exporter

Deploy standalone metrics exporter for ClickHouse cluster telemetry.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: metrics-exporter-config
data:
  config.yaml: |
    watch:
      namespaces: ["production"]
    clickhouse:
      access:
        scheme: "http"
        username: "metrics_user"
        password: "metrics_password"
        port: 8123
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: clickhouse-metrics-exporter
spec:
  replicas: 1
  selector:
    matchLabels:
      app: metrics-exporter
  template:
    metadata:
      labels:
        app: metrics-exporter
    spec:
      containers:
        - name: metrics-exporter
          image: altinity/metrics-exporter:latest
          args:
            - "-config=/config/config.yaml"
            - "-metrics-endpoint=:8888"
          ports:
            - containerPort: 8888
              name: metrics
          volumeMounts:
            - name: config
              mountPath: /config
      volumes:
        - name: config
          configMap:
            name: metrics-exporter-config
---
apiVersion: v1
kind: Service
metadata:
  name: metrics-exporter
spec:
  ports:
    - name: metrics
      port: 8888
      targetPort: 8888
  selector:
    app: metrics-exporter
```

```bash
# Deploy metrics exporter
kubectl apply -f metrics-exporter.yaml

# Verify exporter running
kubectl get pods -l app=metrics-exporter

# Test metrics endpoint
kubectl port-forward svc/metrics-exporter 8888:8888 &
curl http://localhost:8888/metrics

# Check ClickHouse installations being monitored
curl http://localhost:8888/chi | jq .
```

### Use Helm Chart for Installation

Install operator using Helm chart with custom values.

```yaml
# values.yaml
operator:
  image:
    repository: altinity/clickhouse-operator
    tag: 0.25.5

  resources:
    requests:
      memory: "256Mi"
      cpu: "100m"
    limits:
      memory: "512Mi"
      cpu: "500m"

  watchNamespaces:
    - "clickhouse"
    - "production"

metricsExporter:
  enabled: true
  image:
    repository: altinity/metrics-exporter
    tag: 0.25.5

clickhouse:
  access:
    username: "operator"
    password: "operator_secret"

  configuration:
    user:
      default:
        networksIP:
          - "10.0.0.0/8"
          - "172.16.0.0/12"
        password: "changeme"

serviceMonitor:
  enabled: true
  interval: 30s
```

```bash
# Add Altinity Helm repository
helm repo add altinity https://altinity.github.io/clickhouse-operator
helm repo update

# Install with custom values
helm install clickhouse-operator altinity/altinity-clickhouse-operator \
  --namespace clickhouse-system \
  --create-namespace \
  --values values.yaml

# Verify installation
helm list -n clickhouse-system
kubectl get pods -n clickhouse-system

# Upgrade operator
helm upgrade clickhouse-operator altinity/altinity-clickhouse-operator \
  --namespace clickhouse-system \
  --values values.yaml

# Uninstall (preserves CRDs)
helm uninstall clickhouse-operator -n clickhouse-system
```

## Summary

The Altinity Kubernetes Operator for ClickHouse provides comprehensive automation for deploying and managing ClickHouse database clusters on Kubernetes through declarative YAML manifests. Primary use cases include creating highly available replicated clusters with automatic sharding, configuring persistent storage with dynamic provisioning, managing users and access controls with Kubernetes secrets integration, performing rolling upgrades of ClickHouse versions without downtime, and scaling clusters horizontally by adjusting shard and replica counts. The operator handles complex operational tasks like ZooKeeper coordination setup, distributed DDL execution, schema synchronization across replicas, and automatic pod recovery.

Integration patterns involve using the ClickHouseInstallation CRD as the primary interface for cluster specifications, connecting with external ZooKeeper or ClickHouse Keeper clusters for distributed coordination, leveraging Kubernetes StorageClasses for persistent volume provisioning, exposing metrics to Prometheus through ServiceMonitors, and customizing behavior through pod templates, service templates, and volume claim templates. The operator follows GitOps workflows by allowing full cluster definitions in version-controlled YAML files, supports multi-tenancy through namespace isolation, and integrates with standard Kubernetes tooling for logging, monitoring, RBAC, and network policies. Users can deploy via raw manifests, Helm charts, or automated CI/CD pipelines while maintaining full control over ClickHouse configuration through the operator's flexible template system.

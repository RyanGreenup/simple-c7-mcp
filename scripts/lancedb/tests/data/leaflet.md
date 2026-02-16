# Leaflet.heat

Leaflet.heat is a lightweight, high-performance heatmap plugin for the Leaflet mapping library. It enables developers to visualize dense point data on interactive maps through customizable heat layers, making it ideal for displaying geographic patterns, density distributions, and spatial analytics. The plugin uses simpleheat under the hood and implements grid-based clustering for optimal performance even with thousands of data points.

Built as an extension to Leaflet's layer system, the plugin provides a simple API for creating, configuring, and dynamically updating heatmap visualizations. It supports intensity-based coloring, custom gradients, opacity controls, and seamless integration with Leaflet's zoom and pan animations. The plugin is particularly well-suited for applications requiring real-time data visualization, such as tracking events, displaying sensor data, or analyzing geographic distributions.

## API Reference and Code Examples

### L.heatLayer() - Creating a Basic Heatmap

Factory function that constructs a new heatmap layer from an array of latitude/longitude points with optional intensity values.

```javascript
// Include the plugin
<script src="leaflet-heat.js"></script>

// Initialize map
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Create heatmap with point data [lat, lng, intensity]
var heatData = [
    [51.505, -0.09, 0.8],    // High intensity point
    [51.506, -0.10, 0.5],    // Medium intensity
    [51.504, -0.08, 1.0],    // Maximum intensity
    [51.503, -0.11, 0.3],    // Low intensity
    [51.507, -0.09, 0.6]
];

var heat = L.heatLayer(heatData, {
    radius: 25,
    blur: 15,
    maxZoom: 17
}).addTo(map);
```

### Custom Gradient Configuration

Configure custom color gradients to control the visual appearance of heat intensity levels across the heatmap.

```javascript
var map = L.map('map').setView([40.7128, -74.0060], 11);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Define custom gradient from blue (cold) to red (hot)
var customGradient = {
    0.0: 'blue',
    0.3: 'cyan',
    0.5: 'lime',
    0.7: 'yellow',
    1.0: 'red'
};

var trafficData = [
    [40.7580, -73.9855, 0.9],  // Times Square - high traffic
    [40.7489, -73.9680, 0.7],  // Grand Central - medium-high
    [40.7614, -73.9776, 0.5],  // Central Park South
    [40.7128, -74.0060, 0.8]   // Lower Manhattan
];

var heat = L.heatLayer(trafficData, {
    minOpacity: 0.4,
    maxZoom: 15,
    max: 1.0,
    radius: 30,
    blur: 20,
    gradient: customGradient
}).addTo(map);
```

### addLatLng() - Adding Points Dynamically

Add individual points to an existing heatmap layer in real-time, automatically triggering a redraw.

```javascript
var map = L.map('map').setView([37.7749, -122.4194], 12);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Initialize empty heatmap
var heat = L.heatLayer([], {radius: 20}).addTo(map);

// Add points dynamically on map interaction
var isDrawing = true;

map.on('movestart', function() {
    isDrawing = false;
});

map.on('moveend', function() {
    isDrawing = true;
});

map.on('mousemove', function(e) {
    if (isDrawing) {
        // Add point at cursor location with random intensity
        var intensity = Math.random() * 0.5 + 0.5;
        var point = L.latLng(e.latlng.lat, e.latlng.lng, intensity);
        heat.addLatLng(point);
    }
});

// Add points programmatically (e.g., from API)
setTimeout(function() {
    heat.addLatLng([37.7849, -122.4094, 0.8]);
}, 1000);
```

### setLatLngs() - Replacing All Heatmap Data

Replace the entire dataset of the heatmap layer with new points, useful for filtering or updating visualizations.

```javascript
var map = L.map('map').setView([34.0522, -118.2437], 10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

var earthquakeData = [
    [34.0522, -118.2437, 0.6],
    [34.0622, -118.2537, 0.4],
    [34.0422, -118.2337, 0.8]
];

var heat = L.heatLayer(earthquakeData, {radius: 25}).addTo(map);

// Simulate data update (e.g., new sensor readings)
document.getElementById('updateBtn').addEventListener('click', function() {
    var newData = [
        [34.0722, -118.2637, 0.9],  // New high intensity event
        [34.0322, -118.2237, 0.5],
        [34.0522, -118.2437, 0.3]   // Previous location, lower intensity
    ];

    heat.setLatLngs(newData);  // Completely replace dataset
});

// Filter by intensity threshold
document.getElementById('filterBtn').addEventListener('click', function() {
    var filtered = earthquakeData.filter(function(point) {
        return point[2] >= 0.5;  // Only show high intensity points
    });
    heat.setLatLngs(filtered);
});
```

### setOptions() - Updating Heatmap Configuration

Dynamically modify heatmap rendering options without recreating the layer, enabling interactive controls.

```javascript
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

var data = [
    [51.505, -0.09, 0.8],
    [51.506, -0.10, 0.5],
    [51.504, -0.08, 1.0],
    [51.503, -0.11, 0.3]
];

var heat = L.heatLayer(data, {
    radius: 20,
    blur: 15,
    maxZoom: 15
}).addTo(map);

// Dynamic radius control
document.getElementById('radiusSlider').addEventListener('input', function(e) {
    var radius = parseInt(e.target.value);  // e.g., 10-50
    heat.setOptions({radius: radius});
});

// Dynamic blur control
document.getElementById('blurSlider').addEventListener('input', function(e) {
    var blur = parseInt(e.target.value);  // e.g., 5-30
    heat.setOptions({blur: blur});
});

// Toggle gradient presets
document.getElementById('gradientSelect').addEventListener('change', function(e) {
    var gradients = {
        'default': null,
        'cool': {0.4: 'blue', 0.6: 'cyan', 1.0: 'lime'},
        'warm': {0.4: 'yellow', 0.6: 'orange', 1.0: 'red'},
        'purple': {0.4: 'purple', 0.6: 'pink', 1.0: 'white'}
    };
    heat.setOptions({gradient: gradients[e.target.value]});
});
```

### Advanced Configuration Options

Comprehensive example demonstrating all available configuration options for fine-tuned heatmap rendering.

```javascript
var map = L.map('map').setView([48.8566, 2.3522], 12);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Large dataset with varying intensities
var sensorData = [];
for (var i = 0; i < 10000; i++) {
    var lat = 48.8566 + (Math.random() - 0.5) * 0.1;
    var lng = 2.3522 + (Math.random() - 0.5) * 0.1;
    var intensity = Math.random();
    sensorData.push([lat, lng, intensity]);
}

var heat = L.heatLayer(sensorData, {
    // Minimum opacity for the heatmap layer (0.0 - 1.0)
    minOpacity: 0.05,

    // Maximum zoom level at which points reach full intensity
    // Beyond this zoom, intensity doesn't increase further
    maxZoom: 18,

    // Maximum point intensity value for normalization
    // All intensities are scaled relative to this value
    max: 1.0,

    // Radius of each heat point in pixels
    radius: 25,

    // Amount of blur applied to heat points
    blur: 15,

    // Custom color gradient stops (value: color)
    gradient: {
        0.0: 'navy',
        0.25: 'blue',
        0.5: 'green',
        0.75: 'yellow',
        1.0: 'red'
    },

    // Map pane for rendering (controls z-index layering)
    pane: 'overlayPane'
}).addTo(map);

// Performance monitoring
console.log('Heat layer bounds:', heat.getBounds());
console.log('Total points:', sensorData.length);
```

### Working with Leaflet LatLng Objects

Use Leaflet's native LatLng objects instead of arrays for point data, enabling better type safety and integration.

```javascript
var map = L.map('map').setView([35.6762, 139.6503], 11);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Create points using L.latLng objects with altitude (intensity)
var locations = [
    L.latLng(35.6762, 139.6503, 0.9),  // Tokyo Station - high
    L.latLng(35.6895, 139.6917, 0.7),  // Shinjuku - medium-high
    L.latLng(35.6586, 139.7454, 0.6),  // Tokyo Skytree - medium
    L.latLng(35.6585, 139.7432, 0.5)   // Asakusa - medium-low
];

var heat = L.heatLayer(locations, {
    radius: 30,
    blur: 20
}).addTo(map);

// Add points from user clicks
map.on('click', function(e) {
    // Create LatLng with altitude parameter for intensity
    var clickPoint = L.latLng(e.latlng.lat, e.latlng.lng, 0.8);
    heat.addLatLng(clickPoint);
    console.log('Added point:', clickPoint.lat, clickPoint.lng, clickPoint.alt);
});

// Get bounds and fit map to heatmap extent
var bounds = heat.getBounds();
if (bounds.isValid()) {
    map.fitBounds(bounds, {padding: [50, 50]});
}
```

### Real-Time Data Streaming

Stream live data to a heatmap layer, simulating real-time sensor networks or event tracking systems.

```javascript
var map = L.map('map').setView([40.7128, -74.0060], 12);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

var heat = L.heatLayer([], {
    minOpacity: 0.3,
    radius: 20,
    blur: 15,
    max: 1.0
}).addTo(map);

// Simulate streaming data from API/WebSocket
var dataBuffer = [];
var maxBufferSize = 5000;

function streamDataPoint() {
    // Simulate incoming data point
    var lat = 40.7128 + (Math.random() - 0.5) * 0.05;
    var lng = -74.0060 + (Math.random() - 0.5) * 0.05;
    var intensity = Math.random() * 0.5 + 0.5;

    dataBuffer.push([lat, lng, intensity]);

    // Limit buffer size for performance
    if (dataBuffer.length > maxBufferSize) {
        dataBuffer.shift();  // Remove oldest point
    }

    // Update heatmap with current buffer
    heat.setLatLngs(dataBuffer.slice());  // Create copy
}

// Stream 10 points per second
var streamInterval = setInterval(streamDataPoint, 100);

// Control streaming
document.getElementById('pauseBtn').addEventListener('click', function() {
    clearInterval(streamInterval);
});

document.getElementById('resumeBtn').addEventListener('click', function() {
    streamInterval = setInterval(streamDataPoint, 100);
});

document.getElementById('clearBtn').addEventListener('click', function() {
    dataBuffer = [];
    heat.setLatLngs([]);
});
```

## Usage Summary and Integration

Leaflet.heat is primarily used for visualizing geographic density patterns and point distributions on web maps. Common use cases include crime mapping, population density visualization, sensor network data display, earthquake activity tracking, traffic pattern analysis, and customer location heatmaps for business intelligence. The plugin excels at handling large datasets (10,000+ points) while maintaining smooth performance through intelligent grid-based clustering. Its minimal API surface makes it quick to integrate while offering sufficient customization through options like gradient configuration, intensity scaling, and opacity controls.

Integration is straightforward: include the leaflet-heat.js file after Leaflet, create a heatmap layer with your point data, and add it to the map. The plugin integrates seamlessly with Leaflet's event system and layer management, supporting standard operations like adding/removing from the map, dynamic data updates via addLatLng() and setLatLngs(), and runtime configuration changes through setOptions(). For production deployments, the plugin works well with module bundlers and can be combined with other Leaflet plugins. The compact file size (minified bundle includes both simpleheat and the layer implementation) ensures minimal impact on page load times, making it suitable for high-traffic web applications requiring real-time geographic data visualization.

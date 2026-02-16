### Run Binance WebSocket API Spot Script

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/examples/binance_websocket_api_spot/README.md

Executes the main Python script for the Binance WebSocket API Spot. This command starts the application after dependencies and environment variables are set up.

```bash
python binance_websocket_api_spot.py
```

--------------------------------

### Run Jupyter Notebook Server

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/ipynb/README.md

Launches the Jupyter Notebook server from the command line. This command will start a web server and typically open a new tab in your default web browser pointing to the Jupyter Notebook interface.

```bash
jupyter notebook
```

--------------------------------

### Install from GitHub (Latest Release)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Installs the latest release version of the unicorn-binance-websocket-api directly from its GitHub repository using pip. This is useful for getting the most stable recent version.

```bash
pip install git+https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api.git
```

--------------------------------

### Installation using pip (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Instructions for installing the unicorn-binance-websocket-api library using pip, the standard Python package installer. This command fetches the latest stable version from PyPI.

```bash
pip install unicorn-binance-websocket-api

```

--------------------------------

### Install Jupyter with Pip

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/ipynb/README.md

Installs the Jupyter package using pip, the Python package installer. Ensure pip is up-to-date before running this command.

```bash
pip3 install jupyter
```

--------------------------------

### Install unicorn-binance-websocket-api with pip

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/dev/sphinx/source/readme.md

Installs the unicorn-binance-websocket-api package using pip. This is the standard method for installing Python packages and ensures you get the latest version. It may compile locally if pre-compiled wheels are not available for your architecture.

```bash
pip install unicorn-binance-websocket-api
```

--------------------------------

### Install Python Dependencies

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/examples/binance_chain_websocket_best_practice/README.md

Installs necessary Python packages for the Binance Chain WebSocket API project using pip.

```bash
pip install -r requirements.txt
```

--------------------------------

### Install Latest Release (Linux/macOS)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/README.md

Installs the latest stable release of the unicorn-binance-websocket-api library from GitHub using pip. It dynamically fetches the latest tag name for the installation.

```bash
pip install https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-websocket-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?="').tar.gz --upgrade
```

--------------------------------

### Install from Latest Source (Development)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/dev/sphinx/source/readme.md

Installs the latest development version of the unicorn-binance-websocket-api directly from the master branch on GitHub. This is not recommended for production environments as it may be unstable.

```bash
pip install https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/tarball/master --upgrade
```

--------------------------------

### Install from GitHub (Dev-Stage)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Installs the latest development version (dev-stage) of the unicorn-binance-websocket-api from GitHub using pip. This provides access to the newest, potentially unstable features.

```bash
pip install git+https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api.git@dev
```

--------------------------------

### Installation from GitHub Source (Linux/macOS) (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Installs the unicorn-binance-websocket-api library directly from the latest source code on GitHub for Linux and macOS systems using pip.

```bash
pip install git+https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api.git

```

--------------------------------

### Get Start Time (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Retrieves the timestamp indicating when the BinanceWebSocketApiManager instance was initialized. This is useful for tracking the lifecycle of the manager.

```python
get_start_time()
```

--------------------------------

### Get Start Time - Python

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

Retrieves the start time of the BinanceWebSocketApiManager instance. Returns a timestamp representing the start time.

```python
def get_start_time(self):
        """
        Get the start_time of the  BinanceWebSocketApiManager instance

        :return: timestamp
        """
        return self.start_time
```

--------------------------------

### Installation using conda (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Instructions for installing the unicorn-binance-websocket-api library using conda from the Anaconda distribution. This command fetches the package from the Anaconda channels.

```bash
conda install -c conda-forge unicorn-binance-websocket-api

```

--------------------------------

### Get Start Time - Python

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Returns the timestamp when the BinanceWebSocketApiManager was initialized. Useful for calculating uptime.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming bman is an instance of BinanceWebSocketApiManager
# bman = BinanceWebSocketApiManager(exchange_id=...) 
start_time = bman.get_start_time()
print(f"Manager started at: {start_time}")
```

--------------------------------

### Help (BinanceWebSocketApiManager)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/genindex.html

Prints helpful information and usage examples for the BinanceWebSocketApiManager. This is a static method.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Display help information
BinanceWebSocketApiManager.help()

```

--------------------------------

### Get BinanceWebSocketApiManager Start Time

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/modules.html

Returns the timestamp when the BinanceWebSocketApiManager was started. This is useful for calculating uptime or analyzing activity periods.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming binance_manager is an instance of BinanceWebSocketApiManager
# Example usage:
# start_time = binance_manager.get_start_time()
# print(f"Manager Start Time: {start_time}")
```

--------------------------------

### Place Order Response Example

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Example of a successful response from the Binance API after placing an order. It confirms the order details, including order ID, symbol, status, and client order ID.

```json
{
    "id": "3f7df6e3-2df4-44b9-9919-d2f38f90a99a",
    "status": 200,
    "result": {
        "orderId": 325078477,
        "symbol": "BTCUSDT",
        "status": "NEW",
        "clientOrderId": "iCXL1BywlBaf2sesNUrVl3",
        "price": "43187.00",
        "avgPrice": "0.00",
        "origQty": "0.100"
    }
}
```

--------------------------------

### Place New Order Example (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Example of placing a new LIMIT order on Binance WebSocket API. It includes parameters like symbol, side, type, timeInForce, price, and quantity. The `process_response` argument allows for custom handling of incoming data.

```python
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

def handle_message(message):
    print(message)

ws = SpotWebsocketStreamClient(on_message=handle_message)

# Place a new order
ws.new_order(
    symbol="BTCUSDT",
    side="SELL",
    type="LIMIT",
    timeInForce="GTC",
    price="23416.10000000",
    quantity="0.00847000",
    newOrderRespType="FULL",
    recv_window=5000,
    returnResponse=True
)

# Place a new order with custom request ID and stream label
ws.new_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    quantity="0.0005",
    request_id="my_order_123",
    stream_label="order_stream_1"
)

# Place a test order
ws.new_order(symbol="BTCUSDT", side="BUY", type="MARKET", quantity="0.01", test=True)

# Place an iceberg order
ws.new_order(
    symbol="BTCUSDT",
    side="SELL",
    type="LIMIT",
    timeInForce="GTC",
    price="23416.10000000",
    quantity="0.00847000",
    iceberg_qty="0.002",
    newOrderRespType="FULL",
    recv_window=5000,
    returnResponse=True
)

# Place a STOP_LOSS_LIMIT order
ws.new_order(
    symbol="BTCUSDT",
    side="BUY",
    type="STOP_LOSS_LIMIT",
    timeInForce="GTC",
    price="23500.00000000",
    quantity="0.005",
    stopPrice="23550.00000000",
    newOrderRespType="FULL",
    recv_window=5000,
    returnResponse=True
)

# Place a TAKE_PROFIT_LIMIT order
ws.new_order(
    symbol="BTCUSDT",
    side="SELL",
    type="TAKE_PROFIT_LIMIT",
    timeInForce="GTC",
    price="23300.00000000",
    quantity="0.007",
    stopPrice="23250.00000000",
    newOrderRespType="FULL",
    recv_window=5000,
    returnResponse=True
)

# Place an order with trailing delta
ws.new_order(
    symbol="BTCUSDT",
    side="BUY",
    type="STOP_LOSS",
    quantity="0.004",
    stopPrice="23100.00000000",
    trailingDelta=50,
    newOrderRespType="FULL",
    recv_window=5000,
    returnResponse=True
)

# Close the connection
# ws.stop()

```

--------------------------------

### Example JSON for API key and signature

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Shows an example of the JSON structure containing API key, signature, and timestamp required for authenticating with the Binance API.

```json
{
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
    "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
    "timestamp": 1660801715431
}
```

--------------------------------

### Set up Environment Variables

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/examples/binance_websocket_api_futures/README.md

Creates an .env file with Binance API key and secret for authentication.

```bash
BINANCE_API_KEY=12A34BCD5678EFG90HIJKLM12NOP3456QR789STUV0WXYZ
BINANCE_API_SECRET=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

--------------------------------

### GET /api/v1/listenKey

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/api/futures.html

Starts a user data stream on Binance Futures and retrieves a listenKey. This key is essential for receiving real-time updates for your account.

```APIDOC
## GET /api/v1/listenKey

### Description
Initiates a user data stream and obtains a listenKey for receiving real-time account updates from Binance Futures.

### Method
GET

### Endpoint
`/api/v1/listenKey`

### Parameters
#### Query Parameters
- **process_response** (function) - Optional - A callback function to process the received stream data.
- **request_id** (str) - Optional - A custom identifier for the request.
- **return_response** (bool) - Optional - If true, waits for and returns the API response directly. This may increase execution time.
- **stream_id** (str) - Optional - The ID of the stream to send the request to. If not provided, it attempts to find an active stream.
- **stream_label** (str) - Optional - The label of the stream to send the request to. Used only if `stream_id` is not provided.

### Request Example
```json
{
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
  "method": "userDataStream.start",
  "params": {
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
  }
}
```

### Response
#### Success Response (200)
- **id** (str) - The request identifier.
- **status** (int) - The status code of the response.
- **result** (object) - Contains the listenKey.
  - **listenKey** (str) - The listen key for the user data stream.
- **rateLimits** (array) - Information about rate limits.

#### Response Example
```json
{
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
  "status": 200,
  "result": {
    "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"
  },
   "rateLimits": [
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 2400,
      "count": 2
    }
  ]
}
```
```

--------------------------------

### Get BinanceWebSocketApiManager Start Time

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Retrieves the timestamp when the BinanceWebSocketApiManager instance was started. Useful for calculating uptime.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming BinanceWebSocketApiManager is initialized and running
# manager = BinanceWebSocketApiManager(...)

# Get start time
start_time = manager.get_start_time()
print(f"Manager Start Time: {start_time}")
```

--------------------------------

### Start Monitoring API Thread

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

Starts a new thread to run the monitoring API service. It takes host, port, and a warning flag as parameters.

```python
thread = threading.Thread(target=self._start_monitoring_api_thread,
                                  args=(host, port, warn_on_update),
                                  name="monitoring_api")
thread.start()
return True
```

--------------------------------

### Install Latest Release (Linux/macOS)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/dev/sphinx/source/readme.md

Installs the latest stable release of the unicorn-binance-websocket-api from GitHub using pip. It dynamically fetches the latest release tag.

```bash
pip install https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-websocket-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade
```

--------------------------------

### Install Specific Release (Windows)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/dev/sphinx/source/readme.md

Installs a specific version of the unicorn-binance-websocket-api from GitHub using pip. The version number should be replaced with the desired release tag.

```bash
pip install https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/archive/2.10.2.tar.gz --upgrade
```

--------------------------------

### GET /api/v1/userDataStream

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Starts a user data stream to receive real-time updates for your account. Requires a listenKey obtained from this endpoint.

```APIDOC
## GET /api/v1/userDataStream

### Description
Starts a user data stream to receive real-time updates for your account. Requires a listenKey obtained from this endpoint.

### Method
GET

### Endpoint
/api/v1/userDataStream

### Parameters
#### Query Parameters
- **listenKey** (str) - Required - The listen key obtained from the API to start the user data stream.

### Request Example
*This endpoint does not require a request body or specific query parameters in the initial call, but rather relies on a `listenKey` which is obtained via a separate call or implicitly managed.* 

### Response
#### Success Response (200)
- **listenKey** (str) - The listen key to establish the user data stream.

#### Response Example
```json
{
  "listenKey": "your_listen_key_here"
}
```
```

--------------------------------

### Install unicorn-binance-websocket-api using Conda

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/readme.html

Installs the latest version of the unicorn-binance-websocket-api library using conda from Anaconda. This is an alternative package management system.

```bash
conda install -c conda-forge unicorn-binance-websocket-api
```

--------------------------------

### Start Monitoring API Service with Flask (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

Starts a monitoring API service using Flask and Gevent's WSGIServer. It sets up a route that redirects to the project's wiki page for the monitoring API. It also adds a REST server resource for status checks.

```python
def _start_monitoring_api_thread(self, host, port, warn_on_update) -> bool:
        """
        Threaded method that servces the monitoring api

        :param host: IP or hostname to use
        :type host: str
        :param port: Port to use
        :type port: int
        :param warn_on_update: Should the monitoring system report available updates?
        :type warn_on_update: bool

        :return: bool
        """
        logger.info("BinanceWebSocketApiManager._start_monitoring_api_thread() - Starting monitoring API service ...")
        app = Flask(__name__)

        @app.route('/')
        @app.route('/status/')
        def redirect_to_wiki():
            logger.info("BinanceWebSocketApiManager._start_monitoring_api_thread() 200 - "
                        "Visit https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/UNICORN-"
                        "Monitoring-API-Service for further information!")
            return redirect("https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/" 
                            "UNICORN-Monitoring-API-Service", code=302)

        api = Api(app)
        api.add_resource(BinanceWebSocketApiRestServer,
                         "/status/<string:statusformat>/",
                         "/status/<string:statusformat>/<string:checkcommandversion>",
                         resource_class_kwargs={'handler_binance_websocket_api_manager': self,
                                                'warn_on_update': warn_on_update})
        try:
            with app.app_context():
                dispatcher = wsgi.PathInfoDispatcher({'/': app})
                self.monitoring_api_server = wsgi.WSGIServer((host, port), dispatcher)
                self.monitoring_api_server.start()
        except RuntimeError as error_msg:
            logger.critical("BinanceWebSocketApiManager._start_monitoring_api_thread() - Monitoring API service is "
                            "going down! - error_msg: RuntimeError - " + str(error_msg))
            self.stop_monitoring_api()
            return False
        except ResourceWarning as error_msg:
            logger.critical("BinanceWebSocketApiManager._start_monitoring_api_thread() - Monitoring API service is "
                            "going down! - error_msg: ResourceWarning - " + str(error_msg))
            self.stop_monitoring_api()
            return False
        except OSError as error_msg:
            logger.critical("BinanceWebSocketApiManager._start_monitoring_api_thread() - Monitoring API service is "
                            "going down! - error_msg: OSError - " + str(error_msg))
            self.stop_monitoring_api()
            return False
        return True
```

--------------------------------

### BinanceWebSocketApiManager: Starting Stream Management

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Overloads threading.run() to start management functions for the Binance WebSocket API. This is a core method for initiating the manager's operations.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Example usage:
# bman = BinanceWebSocketApiManager()
# bman.run()
```

--------------------------------

### Get UnicornFy Version Functionality (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/changelog.html

Adds `get_version_unicorn_fy()` to retrieve the currently installed version of the unicorn-fy library.

```Python
def get_version_unicorn_fy():
    pass
```

--------------------------------

### Start Monitoring API Server

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Starts a local monitoring API server. This server can be used to observe the status and manage the WebSocket API. Configuration options include the host IP address and port, as well as a flag to control update warnings.

```python
start_monitoring_api(_host='127.0.0.1'_, _port=64201_, _warn_on_update=True_)
```

--------------------------------

### Install unicorn-binance-websocket-api with conda

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/dev/sphinx/source/readme.md

Installs the unicorn-binance-websocket-api package using conda. This method requires adding the 'conda-forge' and 'lucit' channels. It's recommended for users who prefer conda for package management and aims for optimal compatibility and performance.

```bash
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-binance-websocket-api
```

--------------------------------

### Install Python Packages for Binance-Kafka Integration

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/examples/binance_websocket_apache_kafka/README.md

Installs necessary Python packages from a requirements file and the latest version of kafka-python from GitHub to ensure compatibility and access to the latest features.

```bash
pip install -r requirements.txt
```

```bash
pip install git+https://github.com/dpkp/kafka-python.git
```

--------------------------------

### Start User Data Stream (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/api/futures.html

Initiates a user data stream on Binance Futures to get a listenKey. It handles stream ID resolution, payload creation, and sending the request. It also supports processing responses asynchronously via a callback or waiting for a direct response.

```python
def get_listen_key(self, process_response=None, request_id: str = None, return_response: bool = False,
                       stream_id: str = None, stream_label: str = None) -> Union[str, dict, bool]:
    """
    Start user data stream (USER STREAM)

    Get a listenKey to start a UserDataStream.

    Official documentation:

        - https://binance-docs.github.io/apidocs/futures/en/#start-user-data-stream-user-stream

    :param process_response: Provide a function/method to process the received webstream data (callback)
                             of this specific request.
    :type process_response: function
    :param request_id: Provide a custom id for the request
    :type request_id: str
    :param return_response: If `True` the response of the API request is waited for and returned directly.
                            However, this increases the execution time of the function by the duration until the
                            response is received from the Binance API.
    :type return_response: bool
    :param stream_id: ID of a stream to send the request
    :type stream_id: str
    :param stream_label: Label of a stream to send the request. Only used if `stream_id` is not provided!
    :type stream_label: str

    :return: str, dict, bool

    Message sent:

    .. code-block:: json

        {
          "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
          "method": "userDataStream.start",
          "params": {
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
          }
        }

    Response:

    .. code-block:: json

        {
          "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
          "status": 200,
          "result": {
            "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"
          },
           "rateLimits": [
            {
              "rateLimitType": "REQUEST_WEIGHT",
              "interval": "MINUTE",
              "intervalNum": 1,
              "limit": 2400,
              "count": 2
            }
          ]
        }
    """
    if stream_id is None:
        if stream_label is not None:
            stream_id = self._manager.get_stream_id_by_label(stream_label=stream_label)
        else:
            stream_id = self._manager.get_the_one_active_websocket_api()
        if stream_id is None:
            logger.critical(f"BinanceWebSocketApiApiFutures.get_listen_key() - error_msg: No `stream_id` provided "
                            f"or found!")
            return False

    request_id = self._manager.get_new_uuid_id() if request_id is None else request_id
    method = "userDataStream.start"
    params = {"apiKey": self._manager.stream_list[stream_id]['api_key']}

    payload = {"id": request_id,
               "method": method,
               "params": params}

    logger.debug(f"BinanceWebSocketApiApiFutures.get_listen_key() - Created payload: {payload}")

    if self._manager.send_with_stream(stream_id=stream_id, payload=payload) is False:
        self._manager.add_payload_to_stream(stream_id=stream_id, payload=payload)

    if process_response is not None:
        with self._manager.process_response_lock:
            entry = {'callback_function': process_response}
            self._manager.process_response[request_id] = entry

    if return_response is True:
        with self._manager.return_response_lock:
            entry = {'event_return_response': threading.Event()}
            self._manager.return_response[request_id] = entry
        self._manager.return_response[request_id]['event_return_response'].wait()
        with self._manager.return_response_lock:
            response_value = self._manager.return_response[request_id]['response_value']
            del self._manager.return_response[request_id]
        return response_value

    return True
```

--------------------------------

### Start Monitoring API Service

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

Starts the monitoring API service on a specified host and port. This service can be used to monitor the status of the WebSocket API manager.

```APIDOC
## POST /start_monitoring_api

### Description
Starts the monitoring API service on a specified host and port. This service can be used to monitor the status of the WebSocket API manager.

### Method
POST

### Endpoint
/start_monitoring_api

### Parameters
#### Query Parameters
- **host** (str) - Optional - The listening IP address. Defaults to '127.0.0.1'. Use '0.0.0.0' or a specific address.
- **port** (int) - Optional - The listening port number. Defaults to 64201.
- **warn_on_update** (bool) - Optional - If set to `False`, the update warning is disabled. Defaults to True.

### Response
#### Success Response (200)
- **status** (bool) - Indicates if the monitoring API service was successfully started.

### Response Example
```json
{
  "status": true
}
```
```

--------------------------------

### Start Binance WebSocket Connection (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

An asynchronous method to initiate and start a Binance WebSocket API socket connection. This function is part of the BinanceWebSocketApiSocket class.

```python
async def start_socket(self): ...
```

--------------------------------

### Run Binance Futures WebSocket Script

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/examples/binance_websocket_api_futures/README.md

Executes the main Python script for interacting with the Binance WebSocket API for futures.

```bash
python binance_websocket_api_futures.py
```

--------------------------------

### Add Binance.us WebSocket Support (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/changelog.html

Integrates support for Binance.us WebSocket streams, with an accompanying example file `example_binance_us.py`. Enables access to Binance.us market data.

```python
# Example usage for Binance.us WebSocket streams.
# Similar to Futures support, this involves using a specific Binance.us API class.
# from unicorn_binance_websocket_api.binance_us_api import BinanceUsSocketAPI
# 
# async def main():
#     socket_api = BinanceUsSocketAPI()
#     socket_api.subscribe(stream='ethusd@aggTrade')
#     await socket_api.connect()
# 
#     while True:
#         await asyncio.sleep(1)
#         # Process messages...
# 
# # The example_binance_us.py file would contain the full implementation.

```

--------------------------------

### Add Binance.com Futures WebSocket Support (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/changelog.html

Implements support for Binance.com Futures WebSocket streams. Includes example files `example_binance_futures.py` and `example_bookticker.py` demonstrating usage.

```python
# Example usage for Binance.com Futures WebSocket streams.
# This would involve importing the relevant Binance Futures class and establishing a connection.
# from unicorn_binance_websocket_api.binance_futures_api import BinanceFuturesSocketAPI
# 
# async def main():
#     socket_api = BinanceFuturesSocketAPI()
#     socket_api.subscribe(stream='btcusdt@trade')
#     await socket_api.connect()
# 
#     while True:
#         await asyncio.sleep(1)
#         # Process messages...
# 
# # The provided examples (example_binance_futures.py, example_bookticker.py) would contain the actual implementation.

```

--------------------------------

### Create Documentation (Shell Script)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/Info-for-maintainers

Generates project documentation using a shell script. This script likely automates the process of building documentation with Sphinx.

```bash
dev/sphinx/create_docs.sh
```

--------------------------------

### Get BinanceWebSocketApiManager Total Received Bytes

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Retrieves the cumulative number of bytes received by all WebSocket connections since the manager started. This is a measure of total data ingress.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming BinanceWebSocketApiManager is initialized and running
# manager = BinanceWebSocketApiManager(...)

# Get total received bytes
total_bytes = manager.get_total_received_bytes()
print(f"Total Received Bytes: {total_bytes}")
```

--------------------------------

### Get BinanceWebSocketApiManager Total Receives

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Retrieves the cumulative count of all received messages or data packets across all WebSocket connections since the manager started. This indicates the total number of data units processed.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming BinanceWebSocketApiManager is initialized and running
# manager = BinanceWebSocketApiManager(...)

# Get total number of receives
total_receives = manager.get_total_receives()
print(f"Total Receives: {total_receives}")
```

--------------------------------

### Get Latest Release Information (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/modules.html

Fetches information about the latest release of the library.

```python
from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager

# Assuming BinanceWebSocketApiManager is instantiated
# Example usage:
# bwm = BinanceWebSocketApiManager(...)
# release_info = bwm.get_latest_release_info()
```

--------------------------------

### BinanceWebSocketApiManager: Help Method

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

The `help()` method provides assistance or information about the BinanceWebSocketApiManager. It does not take any arguments and returns information relevant to using the manager.

```python
BinanceWebSocketApiManager.help()
```

--------------------------------

### Start Monitoring API Service (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service

Starts a RESTful API service to report the status and performance metrics of the UNICORN Binance WebSocket API Manager. The API is accessible at `http://127.0.0.1:64201/status/icinga/`. It can optionally report its version to receive update information. The `warn_on_update` parameter can disable warnings for available updates.

```python
from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager


# BinanceWebSocketApiManager as BinanceWebSocketApiManager

binance_websocket_api_manager = BinanceWebSocketApiManager(                                                                                      
    exchange_listen_only=False
```

--------------------------------

### Start User Data Stream with Binance Spot API

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Obtains a listenKey to initiate a UserDataStream for real-time trading activity. This is essential for receiving updates on account information and order statuses.

```python
get_listen_key(_process_response=None_, _request_id: str | None = None_, _return_response: bool = False_, _stream_id: str | None = None_, _stream_label: str | None = None_)
```

--------------------------------

### Start New Stream and Stop Old Stream (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

This method creates a new WebSocket stream and, after the new stream has started receiving data, stops the old stream. It handles various parameters for stream configuration, including output format, ping intervals, timeouts, and buffer sizes. The method relies on internal `create_stream` and `wait_till_stream_has_started` methods.

```python
def start_and_switch_stream(self, stream_id, new_channels, new_markets, new_stream_label, new_stream_buffer_name, new_api_key, new_api_secret, new_symbols, new_output, new_ping_interval, new_ping_timeout, new_close_timeout, new_stream_buffer_maxlen):
        """
        :param new_output: set to "dict" to convert the received raw data to a python dict, set to "UnicornFy" to convert
                           with `UnicornFy <https://github.com/oliver-zehentleitner/unicorn-fy>`__ - otherwise
                           the output remains unchanged and gets delivered as received from the endpoints
        :type new_output: str
        :param new_ping_interval: Once the connection is open, a `Ping frame` is sent every
                                  `ping_interval` seconds. This serves as a keepalive. It helps keeping
                                  the connection open, especially in the presence of proxies with short
                                  timeouts on inactive connections. Set `ping_interval` to `None` to
                                  disable this behavior. (default: 20)
                                  This parameter is passed through to the `websockets.client.connect() 
                                  <https://websockets.readthedocs.io/en/stable/api.html?highlight=ping_interval#websockets.client.connect>`__
        :type new_ping_interval: int or None
        :param new_ping_timeout: If the corresponding `Pong frame` isn't received within
                                 `ping_timeout` seconds, the connection is considered unusable and is closed with
                                 code 1011. This ensures that the remote endpoint remains responsive. Set
                                 `ping_timeout` to `None` to disable this behavior. (default: 20)
                                 This parameter is passed through to the `websockets.client.connect() 
                                 <https://websockets.readthedocs.io/en/stable/api.html?highlight=ping_interval#websockets.client.connect>`__
        :type new_ping_timeout: int or None
        :param new_close_timeout: The `close_timeout` parameter defines a maximum wait time in seconds for
                                  completing the closing handshake and terminating the TCP connection. (default: 10)
                                  This parameter is passed through to the `websockets.client.connect() 
                                  <https://websockets.readthedocs.io/en/stable/api.html?highlight=ping_interval#websockets.client.connect>`__
        :type new_close_timeout: int or None
        :param new_stream_buffer_maxlen: Set a max len for the `stream_buffer`. Only used in combination with a non-generic
                                     `stream_buffer`. The generic `stream_buffer` uses always the value of
                                     `BinanceWebSocketApiManager()`.
        :type new_stream_buffer_maxlen: int or None
        :return: stream_id or 'None'
        """
        # starting a new socket and stop the old stream not before the new stream received its first record
        new_stream_id = self.create_stream(new_channels,
                                           new_markets,
                                           new_stream_label,
                                           new_stream_buffer_name,
                                           new_api_key,
                                           new_api_secret,
                                           new_symbols,
                                           new_output,
                                           new_ping_interval,
                                           new_ping_timeout,
                                           new_close_timeout,
                                           new_stream_buffer_maxlen)
        if self.wait_till_stream_has_started(new_stream_id):
            self.stop_stream(stream_id=stream_id, delete_listen_key=False)
        return new_stream_id
```

--------------------------------

### Get Listen Key for Binance User Data Stream (Python)

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/api.html

Initiates a request to get a listenKey for Binance's User Data Stream. It handles stream ID resolution, payload creation, and optional response processing or direct return. Dependencies include the 'copy' module and 'threading'.

```python
import copy
import threading
import logging

logger = logging.getLogger(__name__)

class BinanceWebSocketApiApi:
    def __init__(self, manager):
        self.manager = manager

    def get_listen_key(self, process_response=None, request_id: str = None, return_response: bool = False,
                       stream_id=None, stream_label: str = None) -> bool:
        """
        Get a listenKey to start a UserDataStream.

        Official documentation:

            - https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md#user-data-stream-requests

        :param process_response: Provide a function/method to process the received webstream data (callback)
                                 of this specific request.
        :type process_response: function
        :param request_id: Provide a custom id for the request
        :type request_id: str
        :param return_response: If `True` the response of the API request is waited for and returned directly.
                                However, this increases the execution time of the function by the duration until the
                                response is received from the Binance API.
        :type return_response: bool
        :param stream_id: ID of a stream to send the request
        :type stream_id: str
        :param stream_label: Label of a stream to send the request. Only used if `stream_id` is not provided!
        :type stream_label: str
        :return: bool

        Message sent:

        .. code-block:: json

            {
              "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
              "method": "userDataStream.start",
              "params": {
                "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
              }
            }

        Response:

        .. code-block:: json

            {
              "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
              "status": 200,
              "result": {
                "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"
              },
              "rateLimits": [
                {
                  "rateLimitType": "REQUEST_WEIGHT",
                  "interval": "MINUTE",
                  "intervalNum": 1,
                  "limit": 6000,
                  "count": 2
                }
              ]
            }
        """
        if stream_id is None:
            if stream_label is not None:
                stream_id = self.manager.get_stream_id_by_label(stream_label=stream_label)
            else:
                stream_id = self.manager.get_the_one_active_websocket_api()
            if stream_id is None:
                logger.critical(f"BinanceWebSocketApiApi.get_listen_key() - error_msg: No `stream_id` provided or "
                                f"found!")
                return False

        request_id = self.manager.get_new_uuid_id() if request_id is None else request_id
        method = "userDataStream.start"
        params = {"apiKey": self.manager.stream_list[stream_id]['api_key']}

        payload = {"id": request_id,
                   "method": method,
                   "params": params}

        if self.manager.send_with_stream(stream_id=stream_id, payload=payload) is False:
            self.manager.add_payload_to_stream(stream_id=stream_id, payload=payload)

        if process_response is not None:
            with self.manager.process_response_lock:
                entry = {'callback_function': process_response}
                self.manager.process_response[request_id] = entry

        if return_response is True:
            with self.manager.return_response_lock:
                entry = {'event_return_response': threading.Event()}
                self.manager.return_response[request_id] = entry
            self.manager.return_response[request_id]['event_return_response'].wait()
            with self.manager.return_response_lock:
                response_value = copy.deepcopy(self.manager.return_response[request_id]['response_value'])
                del self.manager.return_response[request_id]
            return response_value

        return True

```

--------------------------------

### Example Usage: Binance WebSocket Stream with Asyncio Queue

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Demonstrates the typical workflow for processing data from a Binance WebSocket stream using an asyncio queue. It shows how to fetch data, print it, and mark the task as done.

```python
while True:
    data = await ubwa.get_stream_data_from_asyncio_queue(stream_id)
    print(data)
    ubwa.asyncio_queue_task_done(stream_id)
```

--------------------------------

### Wait for Stream Start in Python

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/_modules/unicorn_binance_websocket_api/manager.html

This Python function waits until a specific stream has started and received its first data. It checks the stream's last heartbeat and returns `True` once the stream has started. A timeout can be specified to prevent indefinite waiting.

```python
def wait_till_stream_has_started(self, stream_id, timeout: float = 0.0) -> bool:
        """
        Returns `True` as soon a specific stream has started and received its first stream data

        :param stream_id: id of a stream
        :type stream_id: str
        :param timeout: The timeout for how long to wait for the stream to stop. The function aborts if the waiting
                        time is exceeded and returns False.
        :type timeout: float

        :return: bool
        """
        timestamp = self.get_timestamp_unix()
        timeout = timestamp + timeout if timeout != 0.0 else timeout
        logger.debug(f"BinanceWebSocketApiManager.wait_till_stream_has_started({stream_id}) with timeout {timeout} "
                     f"started!")
        try:
            while self.stream_list[stream_id]['last_heartbeat'] is None:
                if self.get_timestamp_unix() > timeout != 0.0:
                    logger.debug(
                        f"BinanceWebSocketApiManager.wait_till_stream_has_started({stream_id}) finished with `False`!")
                    return False
                time.sleep(0.1)
            logger.debug(f"BinanceWebSocketApiManager.wait_till_stream_has_started({stream_id}) finished with `True`!")
            return True
        except KeyError:
            logger.debug(f"BinanceWebSocketApiManager.wait_till_stream_has_started({stream_id}) finished with `False`!")
            return False
```

--------------------------------

### GET /api/v1/ticker/price

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/unicorn_binance_websocket_api.html

Get the current average price for a specific symbol on Binance.

```APIDOC
## GET /api/v1/ticker/price

### Description
Get current average price for a symbol.

### Method
GET

### Endpoint
/api/v1/ticker/price

### Parameters
#### Query Parameters
- **symbol** (str) - Required - The trading symbol to get the average price for.
- **process_response** (function) - Optional - Callback function to process received data.
- **request_id** (str) - Optional - Custom ID for the request.
- **return_response** (bool) - Optional - If True, waits for and returns the response directly.
- **stream_id** (str) - Optional - ID of a stream to send the request.
- **stream_label** (str) - Optional - Label of a stream to send the request.

### Request Example
```json
{
  "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",
  "method": "avgPrice",
  "params": {
    "symbol": "BNBBTC"
  }
}
```

### Response
#### Success Response (200)
- **result** (dict) - Contains the average price details.
  - **mins** (int) - Average price interval in minutes.
  - **price** (str) - The calculated average price.
  - **closeTime** (int) - Timestamp of the last trade used for the average price calculation.
- **rateLimits** (list) - Information about rate limits applicable to the request.

#### Response Example
```json
{
  "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",
  "status": 200,
  "result": {
    "mins": 5,
    "price": "0.01378135",
    "closeTime": 1694061154503
  },
  "rateLimits": [
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 6000,
      "count": 2
    }
  ]
}
```
```

--------------------------------

### Update Example Monitoring Script

Source: https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/blob/master/docs/changelog.html

Modifies the `example_monitoring.py` script. This update likely includes adjustments to better demonstrate or utilize the monitoring capabilities of the Binance websocket API library.

```python
example_monitoring.py
```
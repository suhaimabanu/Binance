### Binance WebSocket Price Monitor

#### Overview:
This project aims to develop a Python script that establishes a real-time connection to the Binance WebSocket to capture and process the prices of selected cryptocurrencies. The captured price data will be stored in a database, and API endpoints will be provided for users to access current prices, historical data, and perform basic statistical analysis.

#### Technical Requirements and Features:
1. **WebSocket Connection:**
   - Establish a connection to the Binance WebSocket and subscribe to the 'trade' WebSocket streams for selected cryptocurrency pairs.
   - Extract price information from each trade message received to monitor real-time prices.
   - Implement efficient Python logic to manage the WebSocket connection and incoming data stream, considering Binance API rate limits.

2. **Data Storage:**
   - Design a database schema optimized for storing captured price data.
   - Organize real-time price information to support rapid access for current price queries and historical price analysis.
   - Use Object-Relational Mapping (ORM) for seamless database interactions.
   
3. **API Endpoints:**
   - Develop 3 RESTful endpoints using Flask or similar:
     1. Query the current price of a specific cryptocurrency from the database.
     2. Retrieve historical price data within a user-specified date range.
     3. Perform basic statistical analyses on stored historical data:
        - Average of all prices.
        - Median price.
        - Standard deviation.
        - Percentage change.
   - Ensure differentiation between real-time data and historical analysis endpoints.
   - Implement error handling for invalid date ranges, requests for unsupported cryptocurrency pairs, etc.

4. **Documentation and Testing:**
   - Provide thorough documentation of the API, including endpoint functionalities, expected parameters, response formats, and example requests/responses.
   - Create a comprehensive suite of unit tests to ensure application functionality and reliability.
   - Optional: Consider caching strategies and database optimizations for handling high request volumes efficiently.

#### Project Deliverables:
- **GitHub Repository:** Complete project available in a GitHub repository.
- **Database Design Documentation:** Detailed documentation of the database schema and design choices.
- **API Documentation:** Comprehensive documentation for all API endpoints, parameters, and usage.
- **README for Deployment:** Overview of the project and detailed deployment instructions.

#### Deployment Instructions:
1. Clone the repository to your local machine.
2. Install necessary dependencies using `pip install -r requirements.txt`.
3. Set up your Binance API key and secret.
4. Run the Python script to establish the WebSocket connection and start monitoring prices.
5. Access API endpoints for querying current prices, retrieving historical data, and performing statistical analysis.


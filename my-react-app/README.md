# My React App

This project is a React application that pulls data from the sales table in a database and displays it in a tabular format. The application color codes the rows to indicate whether a transaction is a buy (in red) or a sell (in green).

## Project Structure

```
my-react-app
├── public
│   ├── index.html
├── src
│   ├── components
│   │   └── SalesTable.js
│   ├── App.js
│   ├── index.js
│   └── styles
│       └── SalesTable.css
├── package.json
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-react-app
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm start
   ```

   This will start the development server and open the application in your default web browser.

## Usage

The application will automatically fetch data from the sales table in the database and display it in the `SalesTable` component. Each row will be color-coded based on the transaction type:
- Buys will be displayed in red.
- Sells will be displayed in green.

## License

This project is licensed under the MIT License.
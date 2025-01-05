import React, { useEffect, useState } from 'react';
import './SalesTable.css';

const SalesTable = () => {
    const [salesData, setSalesData] = useState([]);

    useEffect(() => {
        const fetchSalesData = async () => {
            try {
                const response = await fetch('http://0.0.0.0:4000/api/sales');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setSalesData(data);
            } catch (error) {
                console.error('Error fetching sales data:', error);
            }
        };

        fetchSalesData();
    }, []);

    const tableStyles = {
        width: '100%',
        borderCollapse: 'collapse',
        margin: '20px 0',
        fontSize: '18px',
        textAlign: 'left'
    };

    const thTdStyles = {
        padding: '12px',
        backgroundColor: '#b2e3aa',
        borderBottom: '1px solid #ddd'
    };

    const thStyles = {
        backgroundColor: '#f2f2f2'
    };

    const trHoverStyles = {
        backgroundColor: '#f5f5f5'
    };

    const h1Styles = {
        fontSize: '3em',
        fontFamily: 'Arial, sans-serif',
        color: '#333',
        textAlign: 'center',
        margin: '20px 0',
        fontWeight: 'bold'
    };


    return (
        <div>
            <h1 style={h1Styles}>Sales Data</h1>
            <table style={tableStyles}>
                <thead>
                    <tr>
                        <th style={{ ...thTdStyles, ...thStyles }}>Item</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Type</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Movement</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Action</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Price</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Box</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Papers</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Year</th>
                        <th style={{ ...thTdStyles, ...thStyles }}>Date bought</th>
                    </tr>
                </thead>
                <tbody>
                    {salesData.length === 0 ? (
                        <tr>
                            <td colSpan="9">No data available</td>
                        </tr>
                    ) : (
                        salesData.map((sale, index) => (
                            <tr key={index} className={sale.type === 'buy' ? 'buy' : 'sell'} style={trHoverStyles}>
                                <td style={thTdStyles}>{salesData[0][0]}</td>
                                <td style={thTdStyles}>{salesData[0][1]}</td>
                                <td style={thTdStyles}>{salesData[0][2]}</td>
                                <td style={thTdStyles}>{salesData[0][3]}</td>
                                <td style={thTdStyles}>{salesData[0][4]}</td>
                                <td style={thTdStyles}>{salesData[0][5]}</td>
                                <td style={thTdStyles}>{salesData[0][6]}</td>
                                <td style={thTdStyles}>{salesData[0][7]}</td>
                                <td style={thTdStyles}>{salesData[0][8]}</td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default SalesTable;
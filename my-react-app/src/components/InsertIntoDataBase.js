import React, { useState } from 'react';

const InsertIntoDataBase = () => {
    const [formData, setFormData] = useState({
        field1: 'Tag_Heuer',
        field2: 'Formula_1',
        field3: 'Automatic',
        field4: 'Bought',
        field5: '450',
        field6: 'Yes',
        field7: 'No',
        field8: '2021',
        field9: '2025'
    });

    const formStyles = {
        display: 'flex',
        flexDirection: 'column',
        gap: '5px'
    };

    const formGroupStyles = {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        gap: '10px',
        flex: '5%'
    };

    const labelStyles = {
        marginBottom: '5px',
        minWidth: '40px'
    };

    const inputStyles = {
        padding: '8px',
        border: '1px solid #ccc',
        borderRadius: '4px',
        flex: '1',
        maxWidth: '90px'
    };

    const buttonStyles = {
        padding: '10px 20px',
        backgroundColor: '#007bff',
        color: 'white',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        marginTop: '20px'
    };

    const buttonHoverStyles = {
        backgroundColor: '#0056b3'
    };

    const h1Styles = {
        fontSize: '1.5em',
        fontFamily: 'Arial, sans-serif',
        color: '#333',
        textAlign: 'center',
        margin: '20px 0',
        fontWeight: 'bold'
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        let url = `http://0.0.0.0:4000/api/sales_insert/${formData.field1}/${formData.field2}/${formData.field3}/${formData.field4}/${formData.field5}/${formData.field6}/${formData.field7}/${formData.field8}/${formData.field9}`;
        console.log('URL:', url);
        try {
            const response = await fetch(url, {
                mode: 'no-cors'
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            console.log('Data successfully submitted:', data);
        } catch (error) {
            console.error('Error submitting data:', error);
        }
    };

    const labelNames = ["Brand", "Model", "Movement", "Action", "Price", "Box", "Papers", "Year", "Date of Action"];

    return (
        <div>
            <h1 style={h1Styles}>Insert Data Into Database</h1>
            <form onSubmit={handleSubmit} style={formStyles}>
                <div style={formGroupStyles}>
                    {labelNames.map((label, index) => (
                        <div key={index} style={{ display: 'flex', flexDirection: 'column', flex: '1 1 8%', minWidth: '5px' }}>
                            <label style={labelStyles}>{label}</label>
                            <input
                                type="text"
                                name={`field${index + 1}`}
                                value={formData[`field${index + 1}`]}
                                onChange={handleChange}
                                style={inputStyles}
                            />
                        </div>
                    ))}
                </div>
                <button
                    type="submit"
                    style={buttonStyles}
                    onMouseEnter={(e) => e.target.style.backgroundColor = buttonHoverStyles.backgroundColor}
                    onMouseLeave={(e) => e.target.style.backgroundColor = buttonStyles.backgroundColor}
                >
                    Submit
                </button>
            </form>
        </div>
    );
};

export default InsertIntoDataBase;
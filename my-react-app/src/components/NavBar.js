import React from 'react';

const navBarStyles = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'white',
    padding: '10px 30px',
};

const logoStyles = {
    color: '#333',
    fontFamily: 'Arial, sans-serif',
    textDecoration: 'none',
    fontSize: '1.8em',
    fontWeight: 'bold'
};

const linksListStyles = {
    listStyle: 'none',
    display: 'flex',
    margin: 0,
    padding: 0
};

const linkItemStyles = {
    marginLeft: '20px'
};

const linkStyles = {
    color: '#333',
    textDecoration: 'none',
    fontSize: '1.1em',
    fontFamily: 'Arial, sans-serif',
    padding: '8px 12px',
    borderRadius: '4px',
    transition: 'background-color 0.3s ease'
};

const linkHoverStyles = {
    backgroundColor: '#444'
};

const NavBar = () => {
    return (
        <nav style={navBarStyles}>
            <div className="navbar-logo">
                <a href="/" style={logoStyles}>Ebay Watch Project</a>
            </div>
            <ul style={linksListStyles}>
                <li style={linkItemStyles}>
                    <a href="/" style={linkStyles} onMouseEnter={(e) => e.target.style.backgroundColor = linkHoverStyles.backgroundColor} onMouseLeave={(e) => e.target.style.backgroundColor = ''}>Home</a>
                </li>
                <li style={linkItemStyles}>
                    <a href="/sales" style={linkStyles} onMouseEnter={(e) => e.target.style.backgroundColor = linkHoverStyles.backgroundColor} onMouseLeave={(e) => e.target.style.backgroundColor = ''}>Sales</a>
                </li>
                <li style={linkItemStyles}>
                    <a href="/research" style={linkStyles} onMouseEnter={(e) => e.target.style.backgroundColor = linkHoverStyles.backgroundColor} onMouseLeave={(e) => e.target.style.backgroundColor = ''}>Research</a>
                </li>
                <li style={linkItemStyles}>
                    <a href="/about" style={linkStyles} onMouseEnter={(e) => e.target.style.backgroundColor = linkHoverStyles.backgroundColor} onMouseLeave={(e) => e.target.style.backgroundColor = ''}>About</a>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;
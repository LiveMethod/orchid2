import React, { Component } from 'react';

// Header Bar
//    Scrape Tools
//    Title
//    Search

class Header extends Component {
  render() {
    
    const styles={
      bar: {
        backgroundColor: 'red',
        display: 'flex',
        flexDirection: 'row',
      },
      scrapeTools: {
        backgroundColor: 'yellow',
        flex: '3',
      },
      title: {
        backgroundColor: 'green',
        flex: '1',
        minWidth: 200,
      },
      search: {
        backgroundColor: 'blue',
        flex: '3',
      }
    };

    return (
      <div style={styles.bar}>
        <div style={styles.scrapeTools}>
          Scrape Tools
        </div>
        <div style={styles.title}>
          {this.props.title}
        </div>
        <div style={styles.search}>
          Search
        </div>
      </div>
    );
  }
}

export default Header;

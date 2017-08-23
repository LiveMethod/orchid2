import React, { Component } from 'react';
import '../styles/Header.css';

class Header extends Component {
  render() {
    return (
      <div className="header-bar">
        <div className="scrape-tools">
          Scrape Tools
        </div>
        <div className="title">
          {this.props.title}
        </div>
        <div className="search">
          Search
        </div>
      </div>
    );
  }
}

export default Header;

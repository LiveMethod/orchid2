import React, { Component } from 'react';
import Header from './components/Header';
import MonthSelectBar from './components/MonthSelectBar';
import './styles/App.css';

class App extends Component {
  render() {
    return (
      <div className="orchid-wrap">
        <div className="fixed-header-area">
          <Header title="Header Title" />
          <MonthSelectBar />
        </div>
      </div>
    );
  }
}

export default App;

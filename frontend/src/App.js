import React, { Component } from 'react';
import Header from './Components/Header';
import MonthSelectBar from './Components/MonthSelectBar';

class App extends Component {
  render() {
    return (
      <div className="App">
        {
          // Main Content Area
          //    Efficiency
          //    Month By Day
          //    Necessity By Size

          // Sidebar
          //    Toggle
          //    Transactions
        }
        <Header title="Header Title" />
        <MonthSelectBar />
      </div>
    );
  }
}

export default App;

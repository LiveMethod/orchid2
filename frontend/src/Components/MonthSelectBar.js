import React, { Component } from 'react';
import '../styles/MonthSelectBar.css';
// Month Select Bar
//    Arrow
//    Months
//    Arrow

class MonthSelectBar extends Component {

  render() {
    const fakeMonths = [
      { name: 'jan', month: '01', year: '2016', uncategorized: true, amount: 4098 },
      { name: 'feb', month: '02', year: '2016', uncategorized: true, amount: 6238 },
      { name: 'mar', month: '03', year: '2016', uncategorized: true, amount: 8374 },
      { name: 'apr', month: '04', year: '2016', uncategorized: true, amount: 6944 },
      { name: 'may', month: '05', year: '2016', uncategorized: true, amount: 8347 },
      { name: 'jun', month: '06', year: '2016', uncategorized: true, amount: 3472 },
      { name: 'jul', month: '07', year: '2016', uncategorized: true, amount: 9852 },
      { name: 'aug', month: '08', year: '2016', uncategorized: true, amount: 4622 },
      { name: 'sep', month: '09', year: '2016', uncategorized: true, amount: 8479 },
      { name: 'oct', month: '10', year: '2016', uncategorized: true, amount: 4298 },
      { name: 'nov', month: '11', year: '2016', uncategorized: true, amount: 6384 },
      { name: 'dec', month: '12', year: '2016', uncategorized: true, amount: 1249 },
    ]

    const MonthEntry = (props) => {
      return (
        <div className="month-entry">
          <div className="month-card">
            <span className="month-name">
              {props.name}
            </span>
            <span className="year-name">
              {props.year}
            </span>
          </div>
        </div>
      )
    }

    return (
      <div
        className="month-select-bar"
      >
        <div className="arrow">
          &lt;
        </div>
        <div className="viewport">
          {fakeMonths.map(month =>
            <MonthEntry key={month.name} name={month.name} year={month.year}/>
          )}
        </div>
        <div className="arrow">
          &gt;
        </div>
      </div>
    );
  }
}

export default MonthSelectBar;

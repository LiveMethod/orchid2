import React, { Component } from 'react';

// Month Select Bar
//    Arrow
//    Months
//    Arrow

class MonthSelectBar extends Component {
  render() {

    const styles = {
      bar: {
        backgroundColor: 'orange',
        display: 'flex',
        flexDirection: 'row',
      },
      arrow: {
        backgroundColor: 'yellow',
        width: 40,
        height: 80,
      },
      monthCardViewport: {
        backgroundColor: 'green',
        flex: '1',
        display: 'flex',
        flexDirection: 'row',
        overflow: 'hidden',
      },
      monthCard: {
        backgroundColor: 'white',
        width: 80,
        height: 60,
        margin: '10px 5px',
        textAlign: 'center',
      },
      monthName: {
        width: '100%',
        fontSize: '24px',
        display: 'block',
      },
      yearName: {
        width: '100%',
        fontSize: '14px',
        display: 'block',
      },
    };

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

    const MonthCard = (props) => {
      return (
        <div style={styles.monthCard}>
          <span style={styles.monthName}>
            {props.name}
          </span>
          <span style={styles.yearName}>
            {props.year}
          </span>
        </div>
      )
    }

    return (
      <div style={styles.bar}>
        <div style={styles.arrow}>
          &lt;
        </div>
        <div style={styles.monthCardViewport}>
          {fakeMonths.map(month =>
            <MonthCard key={month.name} name={month.name} year={month.year}/>
          )}
        </div>
        <div style={styles.arrow}>
          &gt;
        </div>
      </div>
    );
  }
}

export default MonthSelectBar;

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';



newFunction();





var name = "Nvidia (NVDA)";




const nvda = [
  { 
  cat: "Sales/Revenue",
  sales2017: 30,
  sales2018: 32,
  percent: 0
}, {
  cat: "Gross Income",
  sales2017: 20,
  sales2018: 40,
  percent: 0
}, {
  cat: "Depreciation",
  sales2017: 80,
  sales2018: 2,
  percent: 0
}];



var company = nvda;

const Percenttd = ({percent}) => {
  
    if(percent > 0){
     return <td class = "pos">{percent}</td>
  } if(percent < 0) {
     return  <td class = "neg">{percent}</td>
  } else {
     return <td>{percent}</td>
  }
}




const TableRow = ({row}) => (
  
  <tr class="tableformat">
    <th key={row.cat}>{row.cat}</th>
    <td key={row.sales2017}>{row.sales2017}</td>
    <td key={row.sales2018}>{row.sales2018}</td>
    <Percenttd percent={((row.sales2018 - row.sales2017) / row.sales2017 * 100).toFixed(2)} />
    
  </tr>
  
)

const Table = ({data}) => (
  <div>
  <h2>{name}</h2>
  <table class = "center">
    <tr class="tableformat">
      <th>
Fiscal year is January-December. All values USD millions.</th>
<th>2017</th>
<th>2018</th>
<th>Percent Change</th>
    </tr>
    {data.map(row =>
      <TableRow row={row} />
    )}
  </table>
  </div>
)



class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      type: "text",
      name: "search"
    }
    
  }
  handleChange = (e) => {
     
     if(e.keyCode === 13) {
       
      this.setState({title: e.target.value})
      
      
     }
    
  }
 

  

  render() {
    
    company = this.state.title;
    
    
    
   

    return <div><input id="searchbar" type="text" name="search"  placeholder={"Search companies by ticker"} 
   
     onKeyDown={this.handleChange} /> <p>{this.state.title}</p></div>;
     
    
  }

  
}





class Page extends React.Component {
  

  render() {
    
    
    return (
      
      <div>
        <h1>Industry Grabber</h1>
        <SearchBar />
    
        <Table data={company} co={name}/>
      </div>
      
    );
    
  }
  
}


ReactDOM.render(
  <Page />,
  document.getElementById("root")
);




// ========================================


import './App.css';
import axios from 'axios';
import {useState,useEffect} from 'react'
function App() {
  const [employee,setEmp]=useState([])
  useEffect(()=>{
    async function getAllEmployees(){
      const emp=await axios.get("http://127.0.0.1:8000/api/employees/")
      console.log(emp.data);
      setEmp(emp.data)
    }
    getAllEmployees()
  },[])

  return (
    <div className="App">
      <h1>This is React </h1>
      <table>
      <thead>
                <th>EmpId</th>
                <th>EmployeeName</th>
                <th>EmployeeNumber</th>
                <th>EmployeeEmail</th>
                <th>Phone Number</th>
                <th>Address</th>
              </thead>
      {
        employee.map((e,i)=>{
          return(
              <tbody>
                <tr>
                  <td>{e.id}</td>
                  <td>{e.name}</td>
                  <td>{e.number}</td>
                  <td>{e.email}</td>
                  <td>{e.mobile}</td>
                  <td>{e.address}</td>
                </tr>
              </tbody>
           
          )
          
        })
      }
      </table>
    
    </div>
  );
}

export default App;

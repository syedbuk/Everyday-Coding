import { useState } from "react";
import data from "./data";
import "./styles.css";

//single selection
//multiple selection

export default function Accordian() {

    const [selection, setSelection] = useState(null);


    function handleSingleSelection(id){

        setSelection(selection === id ? null : id);


    }




    return <div className="wrapper">
        <div className="accordian">

            {data && data.length > 0 ? data.map(dataItem =>

                <div className="item">

                    <div onClick ={handleSingleSelection(dataItem.id)}className="title">
                        <h3>{dataItem.question}</h3>

                    </div><span>+</span>

                   {
                    selection === dataItem.id?<div>{dataItem.answer}</div>:null
                   }

                </div>,) : <div>No data found! </div>
                    
                
                
                
                </div>



    </div>
}
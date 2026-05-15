import { useState } from "react";
import data from "./data";
import "./styles.css";

//single selection
//multiple selection

export default function Accordian() {

    const [selection, setSelection] = useState(null);
    const [enableMultiSelection, setEnableMultiSelection] = useState(false);
    const [multipleSelection, setMultipleSelection] = useState([]);


    function handleSingleSelection(id){

        setSelection(selection === id ? null : id);


    }

    function handleMultipleSelection(id){
        let cpyMultiple= {...multipleSelection};
        const findIndexofCurrentId = cpyMultiple.indexOf(getCurrentId)

        console.log(findIndexofCurrentId);

        if (findIndexofCurrentId === -1) {
            cpyMultiple.push(id);
        } else {
            cpyMultiple.splice(findIndexofCurrentId, 1);


        }

        setMultipleSelection(cpyMultiple)

    }




    return <div className="wrapper">
        <button onClick={() => setEnableMultiSelection(!enableMultiSelection)}>Enable Multi Selection</button>
        <div className="accordian">

            {data && data.length > 0 ? data.map(dataItem =>

                <div className="item">

                    <div onClick ={enableMultiSelection ? () => handleMultipleSelection(dataItem.id) : () => handleSingleSelection(dataItem.id)}className="title">
                        <h3>{dataItem.question}</h3>

                    </div><span>+</span>

                   {
                    enableMultiSelection?multipleSelection.includes(dataItem.id)?<div>{dataItem.answer}</div>:null:selection === dataItem.id?<div>{dataItem.answer}</div>:null
                   }

                </div>) : <div>No data found! </div>
                    
}
                
                
                </div>



    </div>
}
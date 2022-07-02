import React from "react";
import { useState, useEffect } from "react";
import {useLocation, Link} from "react-router-dom";

import { MapContainer, TileLayer} from 'react-leaflet';
import {Polyline, CircleMarker} from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import "./Display.css";


const center = [38.54664607633386, -121.73498483802013,];

var credential = false;

const Display = (props) => {

    const [data, setData] = useState([]);
    const [threshold, setThreshold] = useState(0.5);
    const [show, setShow] = useState(false);

    var green = [];
    var red = [];
    var t = 0.5;


    const getData = async() => {
        const response = await fetch("http://localhost:8000/list", {method : 'GET'});
        const data = await response.json();
        setData(data);
    };

    useEffect(() => {
        getData();
    },[]);

    if (! data.length) return <div>Loading...</div>
    
    const splitData = () => {
        green = [];
        red = [];

        for (var i = 0; i < data.length; i++) {
            const obj = JSON.parse(JSON.stringify(data[i].geometry));
            let n = obj.search('coordinates');
            let m = obj.length;
            let arr = JSON.parse(obj.substring(n+14,m-1));
            if (data[i].risk < threshold) {
                green.push(arr);
            } else {
                red.push(arr);
            }
        }
    };

    const changeThreshold = () => {
        if (t < 0 || t > 1) {
            alert('Invalid threshold !!!')
            return
        }
        setThreshold(t);
        setShow(false);
        splitData();

    }

    splitData();

    return (
        <div>
            <div className="header">
                <button id = 'update' onClick={()=>{setShow(!show)}}>Update Threshold</button>
                {show ?
                <div className="hidden">
                    <input id = "request" placeholder='type new threshold ...' onChange={(event)=> t = event.target.value }></input> 
                    <button id = "confirm" onClick={()=>{changeThreshold();}}> confirm</button>
                </div> 
                : null}

                <p id = 'threshold-display' > Current Threshold : {threshold}</p>
            </div>
            

            <div id = "map">
                <MapContainer center={center} zoom={13} scrollWheelZoom={false} >
                    <CircleMarker center={center}></CircleMarker>
                    <Polyline pathOptions={{color : 'red'}} positions={red} />
                    <Polyline pathOptions={{color : 'green'}} positions={green} />
                    <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    >

                    </TileLayer>
                </MapContainer>
            </div>

            <Link id = "logout" to = {{pathname : '/'}}> Log Out</Link>
        </div>
    );
    
};

export default Display;
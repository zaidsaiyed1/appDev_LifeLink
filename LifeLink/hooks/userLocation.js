import {View,Text,StyleSheet, Button, SafeAreaView } from "react-native";
import * as Location from 'expo-location'
import { useEffect, useState } from "react";
const userLocation=()=>{
const [errorMsg,setErrorMsg] = useState("")
const [longitude,setLongitutde] = useState("")
const [latitude,setLatitude]=useState("")
const [currentAdd,setCurrentAdd] = useState("")
const getLocation=async()=>{
              let {status} = await Location.requestForegroundPermissionsAsync()
              if (status!=='granted') {
                            setErrorMsg("Permission is not granted")
                            return;
              }
              let {coords} = await Location.getCurrentPositionAsync({
                            accuracy: Location.Accuracy.Highest,
              })
              if (coords) {
                        // const {latitude,longitude} = coords;
                        console.log(coords.latitude,coords.longitude)
                        setLatitude(coords.latitude)
                        setLongitutde(coords.longitude)
                        let response = await Location.reverseGeocodeAsync({
                            latitude,
                            longitude,
                        })    
                        const address = response[0].formattedAddress
                        console.log("userlocation",response[0].formattedAddress)
                        setCurrentAdd(address)
                       
                        
              }

}

useEffect(()=>{
              getLocation();
},[])

return { latitude, longitude,currentAdd, errorMsg, getLocation };
}

export default userLocation               
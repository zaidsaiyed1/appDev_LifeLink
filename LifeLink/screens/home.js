import { useNavigation } from "@react-navigation/native";
import {View,Text,StyleSheet, Button, SafeAreaView } from "react-native";
import userLocation from "../hooks/userLocation";
import { useState,useEffect} from "react";
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useRef } from "react";
import {token} from "./login"
import * as SecureStore from 'expo-secure-store'
const HomeScreen=()=>{
  const countRef = useRef(0)
  const { latitude, longitude,currentAdd, errorMsg, getLocation } = userLocation();
  // const {currLatH,currLonH,errorMsg1,getLocation1} = userLocation()
  const navigation = useNavigation()
  const [amdata,setData] = useState([])
  const [loadedData,setLoadedData] = useState([])
  
  

// useEffect(()=>{
  
// },[])



  useEffect(() => {

      const interval = setInterval(() => {
        getLocation()
        loadUpdateCurrentLocation();
      }, 5000);
      return () => clearInterval(interval);
    
  });
 
 
 const saveData = async (data) => {
  try {
    await AsyncStorage.setItem('ambulanceData', JSON.stringify(data));
    console.log("Data saved successfully!");
  } catch (e) {
    console.log("Saving error:", e);
  }
};
const fetchDataUser = async()=>{

}
  const fetchData = async()=>{
const token = await SecureStore.getItemAsync('access');
    const response = await fetch('http://192.168.116.30:8000/api/getUserAmbulance/',{
      method:'GET',
      headers:{
        'Authorization': `Bearer ${token}`,
         'Content-Type': 'application/json',
      }
    })
    const dataJson= await response.json()
    console.log(dataJson)
    // const data = dataJson.find(item => item.amid == 1);
    if (dataJson.data.length>0) {
      const data =  dataJson.data[0]
      setData(data)
      saveData(data)
      setLoadedData(data)
      console.log(data)
    }
   
  }
  

  const loadData = async () => {
    
    try {
      const value = await AsyncStorage.getItem('ambulanceData');
      if (value !== null) {
        const parsedData = JSON.parse(value);
       
        setLoadedData(parsedData)
        console.log("Loaded Data:", parsedData);
      }
    } catch (e) {
      console.log("Loading error:", e);
    }
  };



  const storeCurrentLocation= async()=>{  
 const token = await SecureStore.getItemAsync('access');
    const dataCurrentLoc = {
      ambulanceName: loadedData.amid,
      currLat: parseFloat(latitude),
      currLon: parseFloat(longitude),
      current_Address:currentAdd

    };
   const data  = await fetch('http://192.168.116.30:8000/api/ambulanceCurrentLocations/',{
    
      method:'GET',
      headers:{
        'Authorization': `Bearer ${token}`,
         'Content-Type': 'application/json',
      }
   })
   const dataJson = await data.json();
   const allData = dataJson.data; 
    
    const ambulanceData = allData.find(item => item.ambulanceName === loadedData.amid); // or amdata.amid

    if (!ambulanceData) {
      
      
      
      const responseLoca = await fetch('http://192.168.116.30:8000/api/ambulanceCurrentLocations/',{
        method:'POST',
        headers:{
          'Authorization': `Bearer ${token}`,
          'Content-Type':'application/json',
        },
        body:JSON.stringify(dataCurrentLoc)
      })
      const res =await responseLoca.json()
      console.log(res)
      console.log("datastore")
      
    }
    else{

      console.log("Data is present")
    }
    }
       
        
 
        const loadUpdateCurrentLocation = async()=>{
        const token = await SecureStore.getItemAsync('access');
          try {
            const response = await fetch('http://192.168.116.30:8000/api/ambulanceCurrentLocations/',{
              method:'GET',
      headers:{
        'Authorization': `Bearer ${token}`,
         'Content-Type': 'application/json',}
            });
            const dataJson = await response.json();
            const allData = dataJson.data
            const ambulanceUpdating = allData.find(item => item.ambulanceName === loadedData.amid);
      
            if (!ambulanceUpdating) {
              console.log("Ambulance not found in server.");
              return;
            }
            if (latitude == null || longitude == null) {
              console.log("Waiting for valid location...");
              return;
            }
        
               const formatedLat = parseFloat(latitude.toFixed(3));
            const formatedLon = parseFloat(longitude.toFixed(3));
            const serverLat = parseFloat((ambulanceUpdating.currLat).toFixed(3));
            const serverLon = parseFloat((ambulanceUpdating.currLon).toFixed(3));
            const dataNotification = {
              ambulanceName:loadedData.amid,
              ambulanceCurrLoc:ambulanceUpdating.curAmb,
              notification_title:"Emergency occure!",
             
            }
            if (formatedLat === serverLat && formatedLon === serverLon) {
              countRef.current += 1;
              console.log(`Same location detected. Count: ${countRef.current}`);
              if (countRef.current >= 5) {
                console.log("Ambulance Emergency Detected!");
                const responseNotify = await fetch('http://192.168.116.30:8000/api/notifications/', {
                  method: 'POST',
                  headers: { 
                    'Authorization': `Bearer ${token}`
                    ,'Content-Type': 'application/json' },
                  body: JSON.stringify(dataNotification)
                });
                const res = await responseNotify.text();
                console.log("Notify:", res);
                
                countRef.current = 0; // Reset after emergency detected
              }
            } else {
              countRef.current = 0; // reset count if moved
      
              const dataCurrentLoc = {
                curAmb: ambulanceUpdating.curAmb,
                ambulanceName: amdata.amid,
                currLat: formatedLat,
                currLon: formatedLon,
                current_Address:currentAdd

              };
      
              const responseLoca = await fetch('http://192.168.116.30:8000/api/ambulanceCurrentLocations/', {
                method: 'PATCH',
                headers: { 'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json' },
                body: JSON.stringify(dataCurrentLoc)
              });
              const res = await responseLoca.json();
              console.log("Updated location:", res);
            }
          } catch (e) {
            console.log("Error updating location:", e);
          }
        };
      


  
useEffect(()=>{
  if (latitude != null && longitude != null) {
    storeCurrentLocation();
  } else {
    console.log("Waiting for location...");
  }
}, [latitude, longitude,currentAdd]); 

useEffect(() => {
  fetchData();
  loadData();


}, []);
// useEffect(() => {
  
//   loadUpdateCurrentLocation()
  
// }, []);
return(
  <SafeAreaView>

                <View style={styles.blackContainer}>
                   <Text style={styles.textContainer}>Welcome To LifeLink!</Text>
                   </View>
                   <View>
                     <Button title="See Details" onPress={()=>{navigation.navigate('Ambulance Details',{data:data})}}/>
                      {/* <Text>{latitude}</Text> */}
                      <Button title="Register Ambulance" onPress={()=>{navigation.navigate('Register Ambulance')}}/>
                   </View>
  </SafeAreaView>
                  
                   
);
}
    


const styles = StyleSheet.create({
              blackContainer:{
                height:200,
                width:400,
                backgroundColor:'black', 
                padding:30,
              },
              textContainer:{
              fontSize:25,
               color:'white',
              }
});


export default HomeScreen;



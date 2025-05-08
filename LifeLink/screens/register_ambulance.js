import { use, useState } from "react";
import {View,Text,StyleSheet, Button, SafeAreaView, TextInput} from "react-native";
              
const RegisterNewAmbulance=()=>{
const [Ambulance_Name,setName]=useState('')
const [Ambulance_Number,setNumber] = useState('')  
const [Ambulance_Organization_Name,setOrgaName] = useState('')
const [Ambulance_Driver1,setDriver1] = useState('')
const [Ambulance_Driver2,setDriver2]=useState('')
const [Ambulance_Driver1_Num,setDriver1Num] = useState('')
const [Ambulance_Driver2_Num,setDriver2Num] = useState('')

const handleAddAmbulance= async()=>{
const data = {
              ambulanceName: Ambulance_Name,
              ambulanceNumber: Ambulance_Number,
              ambulanceOrgaName: Ambulance_Organization_Name,
              ambulanceDriverName: Ambulance_Driver1,
              ambulanceDriver2Name: Ambulance_Driver2,
              ambulanceDriverNum: Ambulance_Driver1_Num,
              ambulanceDriver2Num: Ambulance_Driver2_Num
              
}
const response = await fetch('http://192.168.1.10:8000/api/ambulances/',{
              method:'POST',
              headers:{
                            'Content-Type':'application/json',
              },
              body:JSON.stringify(data)
})
const res =await response.json()
console.log(res)
              
}
return (
              <View style={styles.screen}>
                            <TextInput value={Ambulance_Name} onChangeText={setName}
                             placeholder="Enter Ambulance Name" style={styles.input} />
                              <TextInput value={Ambulance_Number} onChangeText={setNumber}
                             placeholder="Enter Ambulance Number Plate Number" style={styles.input} />
                              <TextInput value={Ambulance_Organization_Name} onChangeText={setOrgaName}
                             placeholder="Enter Ambulance Organization Name" style={styles.input} />
                              <TextInput value={Ambulance_Driver1} onChangeText={setDriver1}
                             placeholder="Enter Ambulance Main Driver Name" style={styles.input} />
                              <TextInput value={Ambulance_Driver2} onChangeText={setDriver2}
                             placeholder="Enter Ambulance Secondary Driver Name" style={styles.input} />
                             <TextInput value={Ambulance_Driver1_Num} onChangeText={setDriver1Num}
                             placeholder="Enter Ambulance Main Driver Mobile Number" style={styles.input} />
                              <TextInput value={Ambulance_Driver2_Num} onChangeText={setDriver2Num}
                             placeholder="Enter Ambulance Secondary Driver Mobile Number" style={styles.input} />
                             <Button title="Add Ambulance" onPress={handleAddAmbulance}/>
                 
              </View>
)

}
const styles = StyleSheet.create({
              screen:{
                            padding:20,
              },
              input:{
                            height:40,
                            borderWidth:1,
                            borderRadius:5,
                            padding:10,
                            backgroundColor:'white',
                            marginBottom:10,
              }
})
export default RegisterNewAmbulance
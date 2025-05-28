import { useNavigation } from "@react-navigation/native";
import { use, useContext, useState,  useEffect } from "react";
import {View,Text,StyleSheet, Button, SafeAreaView, TextInput} from "react-native";
import * as SecureStore from 'expo-secure-store'
import HomeScreen from "./home";
import { useAuth } from '../auth-context';
const LoginScreen=()=>{
              const navigation = useNavigation()
              const [email,setEmail]=useState('')
              const [password,setPass] = useState('')
              const [SecurePassword,setSecurePass] = useState(true)  
              const [error,setError] = useState('')
               const { setIsLoggedIn } = useAuth();
              const setTokens = async (access, refresh) => {
  await SecureStore.setItemAsync('access', access);
  await SecureStore.setItemAsync('refresh', refresh);
  console.log("Tokens stored:", { access, refresh });
};

 const checkLoginStatus = async () => {
    const access = await SecureStore.getItemAsync('access');
    const refresh = await SecureStore.getItemAsync('refresh');
    if (access && refresh) {
      console.log("User already logged in, redirecting...");
      //  navigation.navigate("HomeStack",{
      //           screen:'Home'
      //          })  
    }
  };

  useEffect(() => {
    checkLoginStatus();
  }, []);
const handleLogin= async()=>{
const data = {
              email: email,
              password: password,
              
              
}
const response = await fetch('http:///192.168.116.30:8000/api/LoginUserView/',{
              method:'POST',
              headers:{
                            'Content-Type':'application/json',
              },
              body:JSON.stringify(data)
}).then(response=>{
              if (response.ok) {
                            return response.json()
              }
              else{
                            setError("unable to login Re-enter data")
                            throw response.json()
              }
}).then(json=>{
              setTokens(json.token.access, json.token.refresh);
             setIsLoggedIn(true); 
              //  navigation.navigate("HomeStack",{
              //   screen:'Home'
              //  })
})
// const res =await response.json()
// console.log(res)
// if (res=='Invalid Credentials') {
//               console.log("invalid data")
// }
// else{

//               navigation.navigate("HomeStack")
// }
              
}
       
              return (
                            <View style={styles.screen}>
                                          <TextInput value={email} onChangeText={setEmail}
                                           placeholder="Enter Email" style={styles.input} />
                                            <TextInput secureTextEntry={SecurePassword} value={password} onChangeText={setPass}
                                           placeholder="Enter your password" style={styles.input} />
                                           
                                           <Button title="Login" onPress={handleLogin}/>
                                           <Text>{error}</Text>
                               
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

export default LoginScreen
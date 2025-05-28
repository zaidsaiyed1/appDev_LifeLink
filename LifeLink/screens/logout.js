import { useNavigation } from "@react-navigation/native";
import { use, useContext, useState,  useEffect } from "react";
import {View,Text,StyleSheet, Button, SafeAreaView, TextInput,Alert} from "react-native";
import * as SecureStore from 'expo-secure-store'
import { useAuth } from "../auth-context"; 

const LogoutScreen=()=>{

const { setIsLoggedIn } = useAuth();
   
const handleLogout = async () => {
    Alert.alert(
      "Logout",
      "Are you sure you want to logout?",
      [
        { text: "Cancel", style: "cancel" },
        {
          text: "Logout",
          style: "destructive",
          onPress: async () => {
            await SecureStore.deleteItemAsync('access');
            await SecureStore.deleteItemAsync('refresh');
             setIsLoggedIn(false);
          }
        }
      ]
    );
  };

  return (<View>

    <Text>Are you sure you want to Logout</Text>
    <Button title="Logout" onPress={handleLogout} color="red" />
  </View>
  );  
}




export default LogoutScreen
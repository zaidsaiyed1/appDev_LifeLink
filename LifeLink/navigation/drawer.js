import { createDrawerNavigator } from '@react-navigation/drawer';
import AmbulanceDetails from '../screens/ambulancedetails';
import HomeScreen from '../screens/home';
import { HomeStack ,AmbulanceStack, LoginStack, LogoutStack} from './stack';
import isLoggedIn from '../screens/login'
import { useState,useEffect} from "react";
import { useNavigation } from "@react-navigation/native";
import { useAuth } from '../auth-context';
const Drawer = createDrawerNavigator();

export const MyDrawer=()=>{
   const { isLoggedIn } = useAuth();

  return (
    <Drawer.Navigator screenOptions={{ headerShown: false }}>
      {isLoggedIn ? (
        <>
          <Drawer.Screen name="HomeStack" component={HomeStack} options={{ title: 'Home' }} />
          <Drawer.Screen name="AmbulanceStack" component={AmbulanceStack} options={{ title: 'Ambulance Details' }} />
          <Drawer.Screen name="LogoutStack" component={LogoutStack} options={{ title: 'Logout' }} />
        </>
      ) : (
        <Drawer.Screen name="LoginStack" component={LoginStack} options={{ title: 'Login Page' }} />
      )}
       </Drawer.Navigator>
  );
}
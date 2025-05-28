// import 'react-native-reanimated';
// import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { AuthProvider } from './auth-context'
import { MyDrawer } from './navigation/drawer';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useState,useEffect} from "react";
import {LoginStack} from './navigation/stack';
export default function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Get login status from storage or any auth provider
    const checkLogin = async () => {
      const token = await AsyncStorage.getItem('token'); // example
      setIsLoggedIn(!!token);
    };

    checkLogin();
  }, []);

  return (
   <NavigationContainer>
    {/* <HomeStack /> */}
    {/* <MyDrawer /> */}
       <AuthProvider>
        <MyDrawer />
      </AuthProvider>
   </NavigationContainer>
  );
}
// 
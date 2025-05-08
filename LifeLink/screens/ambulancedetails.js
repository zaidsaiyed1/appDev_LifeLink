import { useNavigation, useRoute } from "@react-navigation/native";
import { useLayoutEffect } from "react";
import {View,Text,StyleSheet} from "react-native";
import { HeaderBackButton } from "@react-navigation/elements";
const AmbulanceDetails=()=>{
const route =useRoute();
const {data} =route.params;
const navigation = useNavigation()
useLayoutEffect(()=>{
     navigation.setOptions({
          headerTitle:"Ambulance Details",
          headerLeft:()=>(
               <HeaderBackButton 
               tintColor="black" 
               onPress={()=>navigation.goBack()}/>
          )
     },[])
})
   return(
               
                   <View>
              <Text>Hospital_Name:{data.ambulanceOrgaName}</Text>
              <Text>Ambulance_Number:{data.ambulanceNumber}</Text>
    
                   </View>
);
}


export default AmbulanceDetails;


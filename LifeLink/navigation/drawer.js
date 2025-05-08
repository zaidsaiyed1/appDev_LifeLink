import { createDrawerNavigator } from '@react-navigation/drawer';
import AmbulanceDetails from '../screens/ambulancedetails';
import HomeScreen from '../screens/home';
import { HomeStack ,AmbulanceStack} from './stack';
import { DUMMY_DATA } from "../data/dummy";

const Drawer = createDrawerNavigator();

export const MyDrawer=()=>{
  return (
    <Drawer.Navigator screenOptions={{headerShown:false}}>
      <Drawer.Screen name="HomeStack" component={HomeStack} options={{title:'Home'}} />
      <Drawer.Screen name="AmbulanceStack" component={AmbulanceStack} options={{title:'Ambulance Details'}}/>

    </Drawer.Navigator>
  );
}
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/home';

import AmbulanceDetails from '../screens/ambulancedetails';
import { navOptions } from './optionns';
import { useNavigation } from '@react-navigation/native';
import RegisterNewAmbulance from '../screens/register_ambulance';

const Stack = createStackNavigator();

export const HomeStack=()=> {
  const navigation = useNavigation()
  return (
    <Stack.Navigator screenOptions={()=>navOptions(navigation)}>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Ambulance Details" component={AmbulanceDetails} />
      <Stack.Screen name="Register Ambulance" component={RegisterNewAmbulance} />
    </Stack.Navigator>
  );
}
export const AmbulanceStack=()=> {
  const navigation = useNavigation()
  return (
    <Stack.Navigator screenOptions={()=>navOptions(navigation)}>
      <Stack.Screen name="Ambulance Details" component={AmbulanceDetails} />
    </Stack.Navigator>
  );
}
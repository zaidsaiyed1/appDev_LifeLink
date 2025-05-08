import { TouchableOpacity } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export const navOptions = (nav) => {
  return {
    headerRight: () => (
      <TouchableOpacity onPress={() => nav.toggleDrawer()}
      style={{ marginRight: 10 }}
      >
        <Ionicons name="menu" size={32} color="black" />
      </TouchableOpacity>
    ),
  };
};
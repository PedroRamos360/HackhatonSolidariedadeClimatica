import React from "react";
import { GoogleMap, useLoadScript } from "@react-google-maps/api";
import { REACT_APP_GOOGLE_MAPS_KEY } from "../constants/constants";

const MapComponent = ({ selectedLocation }) => {
    const { isLoaded, loadError: error } = useLoadScript({
        googleMapsApiKey: REACT_APP_GOOGLE_MAPS_KEY
    });
    const mapRef = React.useRef();
    const onMapLoad = React.useCallback((map) => {
        mapRef.current = map;
    }, []);
    const loading = !isLoaded;

    if (loading) {
        return <p>Loading...</p>; // Retornando um elemento JSX em vez de uma string
    }
    if (error) {
        return <p>Error</p>; // Retornando um elemento JSX em vez de uma string
    }

    return (
        <div style={{ marginTop: "20px" }}>
            <GoogleMap
                mapContainerStyle={{
                    height: '400px',
                }}
                center={selectedLocation}
                zoom={10}
                onLoad={onMapLoad}
            ></GoogleMap>
        </div>
    );
};

export default MapComponent;
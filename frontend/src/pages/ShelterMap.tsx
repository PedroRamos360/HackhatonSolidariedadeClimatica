import React, { useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';

mapboxgl.accessToken = 'pk.eyJ1Ijoiam9yZGFub3hhdmllciIsImEiOiJjbHdmcnVuaDkxeHdmMnFraHpvNXY3OWMxIn0.K4euWXNnd04YMRAHOX05UQ';

export const ShelterMap = () => {
    const mapContainer = useRef(null);

    useEffect(() => {
        if (mapContainer.current) {
            const map = new mapboxgl.Map({
                container: mapContainer.current,
                style: 'mapbox://styles/mapbox/streets-v11',
                center: [-74.5, 40],
                zoom: 9
            });

            new mapboxgl.Marker().setLngLat([-74.5, 40]).addTo(map);
            new mapboxgl.Marker().setLngLat([-74.6, 40.1]).addTo(map);
            new mapboxgl.Marker().setLngLat([-74.4, 40.2]).addTo(map);

            return () => map.remove();
        }
    }, []);

    return (
        <div ref={mapContainer} style={{ width: '100%', height: '100vh' }} />
    );
};
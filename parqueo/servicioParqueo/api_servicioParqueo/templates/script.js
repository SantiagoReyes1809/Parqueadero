try {
    fetch('/api_servicioParqueo/views')
        .then(response => response.json())
        .then(data => updateParkingLotInfo(data));
} catch (error) {
    console.error('Error fetching parking lot data:', error);
    
}
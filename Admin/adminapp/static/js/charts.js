document.addEventListener('DOMContentLoaded', function() {
    // Only initialize chart if the element exists
    const chartElement = document.getElementById('myChart');
    if (chartElement) {
        const ctx = chartElement.getContext('2d');
        
        // Default data
        let chartData = {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            datasets: [{
                label: 'Revenue',
                data: [12, 19, 3, 5, 15],
                backgroundColor: 'rgba(0, 255, 255, 0.2)',
                borderColor: '#00ffff',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        };
        
        // Create chart
        const myChart = new Chart(ctx, {
            type: 'line',
            data: chartData,
            options: {
                plugins: {
                    legend: {
                        labels: {
                            color: '#fff'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: { color: '#fff' },
                        grid: { color: '#444' }
                    },
                    y: {
                        ticks: { color: '#fff' },
                        grid: { color: '#444' }
                    }
                }
            }
        });
        
        // Function to update chart data
        async function updateChart() {
            try {
                const response = await fetch('/api/stats/');
                if (response.ok) {
                    const data = await response.json();
                    if (data.values && data.values.length > 0) {
                        myChart.data.datasets[0].data = data.values;
                        myChart.update();
                    }
                }
            } catch (error) {
                console.log('Error fetching chart data:', error);
            }
        }
        
        // Initial load of data
        updateChart();
        
        // Refresh every 5 seconds
        setInterval(updateChart, 5000);
    }
});
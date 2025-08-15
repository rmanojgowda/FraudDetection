const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Example route for detecting fraud
app.post('/fraud-detection', async (req, res) => {
    const { card_number, transaction_value } = req.body;

    // Validate inputs (simple validation)
    if (!card_number || !transaction_value) {
        return res.status(400).json({ error: 'Card number and transaction value are required.' });
    }

    try {
        // Replace with your actual ngrok URL from Colab
        const colabApiUrl = 'http://<ngrok-url>.ngrok.io/detect_fraud';
        
        // Call Google Colab fraud detection API
        const colabApiResponse = await axios.post(colabApiUrl, {
            card_number: card_number,
            transaction_value: transaction_value
        });

        // Check fraud status and send response back
        const fraudStatus = colabApiResponse.data.fraud_status;
        if (fraudStatus === 'fraud') {
            res.status(200).json({ message: 'Fraud detected! Payment not processed.', status: 'fraud' });
        } else {
            res.status(200).json({ message: 'Payment is safe.', status: 'safe' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

import { createClient } from 'redis';

const subscriberClient = createClient();

subscriberClient.on('connect', () => {
  console.log('Redis client connected to the server');
});
  
subscriberClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

subscriberClient.subscribe('holberton school channel');

subscriberClient.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    subscriberClient.unsubscribe('holberton school channel');
    subscriberClient.end(true);
  }
});
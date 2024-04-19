<script lang="ts">
	import { Card } from 'flowbite-svelte';
	import { spring } from 'svelte/motion';
	import { fetchEvents } from '../api'; // Importing the fetchEvents function
  import { onMount } from 'svelte';
  
	let events: any[] = []; // Initialize an empty array to hold the fetched events

	// Fetch events when the component is mounted
	onMount(async () => {
	  try {
		events = await fetchEvents();
	  } catch (error) {
		console.error('Error fetching events:', error);
	  }
	});
  </script>
  
  <div class="event-card">
	{#each events as event}
	  <Card href="/cards">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{event.event_name}</h5>
		<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">Created on: {event.created_on}</p>
	  </Card>
	{/each}
  </div>
  
  <style>
	.event-card {
	  display: flex;
	  border-top: 1px solid rgba(0, 0, 0, 0.1);
	  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
	  margin: 1rem 0;
	}
  </style>
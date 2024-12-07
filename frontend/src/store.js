import { writable } from "svelte/store";

// Simple authentication state
export const isAuthenticated = writable(false);

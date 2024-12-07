<template>
  <v-container>
    <v-row class="w-100">
      <v-col cols="12" md="8">
        <!-- File upload input -->
        <v-file-input
          v-model="file"
          label="Choose a file"
          accept=".csv,.xlsx,.txt,.json"
          @change="handleFileChange"
          show-size
          class="w-100"
        />
      </v-col>
    </v-row>

    <v-row v-if="file">
      <v-col>
        <v-alert type="success" :border="left" colored-border>
          File successfully selected: <strong>{{ file.name }}</strong>
        </v-alert>
      </v-col>
    </v-row>

    <!-- You can add further actions like uploading the file to a server, or showing a preview of the file -->
    <v-row v-if="file">
      <v-col>
        <v-btn @click="uploadFile" color="primary">Upload File</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

const file = ref(null);

// Handle file change (when the user selects a file)
const handleFileChange = (newFile) => {
  console.log("File selected:", newFile);
};

// Upload the file (this can be adjusted to upload to a server or handle the file in another way)
const uploadFile = () => {
  if (file.value) {
    // Example: Here you would send the file to your server using fetch, axios, etc.
    console.log("Uploading file:", file.value);

    // Simulate file upload (replace this with real upload logic)
    setTimeout(() => {
      alert("File uploaded successfully!");
      // Reset the file input after successful upload
      file.value = null;
    }, 1000);
  } else {
    alert("No file selected!");
  }
};
</script>

<style scoped>
/* Optional: Add custom styling if needed */
</style>

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

// Upload the file using Fetch API
const uploadFile = async () => {
  if (file.value) {
    // Create a FormData object to send the file in a POST request
    const formData = new FormData();
    formData.append("file", file.value); // Append the file to the FormData object

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const result = await response.json();

      if (response.ok) {
        alert(`File uploaded successfully!`);
        console.log(result);
      } else {
        alert(`Error: ${result.error}`);
      }

      // Reset the file input after successful upload
      file.value = null;
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("An error occurred during file upload.");
    }
  } else {
    alert("No file selected!");
  }
};
</script>

<style scoped>
/* Optional: Add custom styling if needed */
</style>

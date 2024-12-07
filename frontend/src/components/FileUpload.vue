<template>
  <v-container>
    <!-- File input row -->
    <v-row class="w-100">
      <v-col cols="12" md="8">
        <v-file-input
          v-model="file"
          label="Choose a file"
          accept=".csv,.xlsx,.txt,.json"
          show-size
          class="w-100"
        />
      </v-col>
    </v-row>

    <!-- Selected file alert -->
    <v-row v-if="file">
      <v-col>
        <v-alert type="info" :border="left" colored-border>
          File selected: <strong>{{ file.name }}</strong>
        </v-alert>
      </v-col>
    </v-row>

    <!-- Upload button -->
    <v-row v-if="file">
      <v-col>
        <v-btn
          @click="uploadFile"
          color="primary"
          :loading="isUploading"
          :disabled="isUploading"
        >
          Upload File
        </v-btn>
      </v-col>
    </v-row>

    <!-- Success or error response -->
    <v-row v-if="response">
      <v-col>
        <v-alert type="success" v-if="response.success" colored-border>
          {{ response.message }}
        </v-alert>
        <v-alert type="error" v-else colored-border>
          {{ response.error }}
        </v-alert>
      </v-col>
    </v-row>

    <!-- Display file analysis -->
    <v-row v-if="response?.analysis">
      <v-row class="mt-2 mb-3"
        ><v-col cols="12">
          <h3>File Analysis</h3>

          <p>
            <strong>Shape:</strong> {{ response.analysis.shape.join(" x ") }}
          </p>
          <p>
            <strong>Columns:</strong> {{ response.analysis.columns.join(", ") }}
          </p></v-col
        ></v-row
      >
      <v-row class="mb-3 w-100">
        <v-col cols="12">
          <h3>Wine Counts</h3>
          <v-simple-table class="spaced-table">
            <thead>
              <tr>
                <th class="px-4 py-2">Wine Type</th>
                <th class="px-4 py-2">Count</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(count, type) in response.analysis.wine_counts"
                :key="type"
              >
                <td class="px-4 py-2">{{ type }}</td>
                <td class="px-4 py-2">{{ count }}</td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-col>
      </v-row>
      <v-row>
        <v-simple-table class="spaced-table">
          <thead>
            <tr>
              <th
                v-for="col in Object.keys(response.analysis.head[0])"
                :key="col"
              >
                {{ col }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="row in response.analysis.head"
              :key="row.id"
              class="ml-1"
            >
              <td v-for="value in Object.values(row)" :key="value" class="ml-3">
                {{ value }}
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-row>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";

// Reactive state variables
const file = ref(null);
const isUploading = ref(false);
const response = ref(null);

// Upload file function
const uploadFile = async () => {
  if (file.value) {
    // Reset response
    response.value = null;

    // Prepare form data for POST request
    const formData = new FormData();
    formData.append("file", file.value);

    // Uploading state
    isUploading.value = true;

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const result = await res.json();

      if (res.ok) {
        response.value = { success: true, ...result };
      } else {
        response.value = { success: false, error: result.error };
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      response.value = {
        success: false,
        error: "An error occurred while uploading the file.",
      };
    } finally {
      // Reset the file input and stop loading
      file.value = null;
      isUploading.value = false;
    }
  } else {
    alert("Please select a file to upload.");
  }
};
</script>

<style scoped>
.spaced-table th {
  text-align: left;
  font-weight: bold;
  padding: 12px 16px;
  border: 1px solid #ccc;
  border-collapse: collapse;
}

.spaced-table td {
  padding: 12px 16px;
  border: 1px solid #ccc;
  border-collapse: collapse;
}
</style>

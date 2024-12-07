<template>
  <v-app>
    <v-container fluid>
      <NavBar />

      <v-main class="d-flex justify-center align-center">
        <div class="w-100 ma-10">
          <router-view />
        </div>
      </v-main>
    </v-container>
  </v-app>
</template>

<script setup></script>

<style scoped></style>

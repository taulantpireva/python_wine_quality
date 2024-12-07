<template>
  <v-app>
    <v-main>
      <NavBar />
      <DefaultLayout><router-view /></DefaultLayout>
    </v-main>
  </v-app>
</template>

<script setup>
import DefaultLayout from "./components/defaultLayout.vue";

//
</script>

<template>
  <v-navigation-drawer>
    <v-list>
      <v-list-item> </v-list-item>
    </v-list>
    <v-divider></v-divider>

    <v-list density="compact" nav>
      <v-list-item
        title="Data Exploration"
        value="Home"
        :to="'/'"
      ></v-list-item>
      <v-list-item
        title="Data Unifying & Transformation"
        value="uni_transform"
        :to="'/uni_transform'"
      ></v-list-item>
      <v-list-item
        title="Data Cleansing"
        value="data_cleansing"
        :to="'/data_cleansing'"
      ></v-list-item>
      <v-list-item
        title="Analysis & Validation"
        value="analysis_validation"
        :to="'/analysis_validation'"
      ></v-list-item>
      <v-list-item
        title="Feature Selection"
        value="feature_selection"
        :to="'/feature_selection'"
      ></v-list-item>
      <v-list-item
        title="ML Model Generation"
        value="ml_model"
        :to="'/ml_model'"
      ></v-list-item>
      <v-list-item title="XAI" value="xai" :to="'/xai'"></v-list-item>
      <v-list-item
        title="Our Project"
        value="project"
        :to="'/project'"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

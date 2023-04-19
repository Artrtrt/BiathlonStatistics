<template>
  <div style="height: 100%">
    <i-container class="_margin-bottom-1 _padding-bottom-1">
      <!-- <div style="float: right; padding-right: -30px;">
        <input class="search" style="width: 300px;" placeholder="Поиск по чемпионату" />
      </div> -->
      <div id="title" class="_padding-top-1 _margin-bottom-1">
        <a>Список сезонов</a>
      </div>
      <div style="background-color: #e8eeffc2; border-radius: 20px;" class="_padding-1">
        <div v-for="(season, indseason) in model.data.app.seasonList" :key="indseason"
          class="_margin-bottom-2 season-title _padding-top-1 _padding-bottom-1" style="background-color: #e8eeffc2; border-radius: 20px;">
          <i-container>
            <i-row>
              <i-column>{{ season.title }} {{ season.year }}</i-column>
            </i-row>
            <hr>
            <i-container>
              <i-list-group :bordered="false" style=" background-color: rgba(232, 238, 255, 0.76)">
                <i-list-group-item v-for="(competition, indcomp) in season.competitionList" :key="indcomp"
                  class="competition-title" :href="`/competiton/${indseason}${indcomp}`" style="color: #233567;">
                  <a>{{ competition.title }}</a>
                    <a style="float:right" class="date">{{ competition.date }}</a>
                </i-list-group-item>
              </i-list-group>
            </i-container>
          </i-container>
        </div>
      </div>
    </i-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";

export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,
      active: [],
    };
  },
  methods: {
  },
});
</script>

<style scoped>
#title a {
  color: #233567;
  font-size: 40px;
}

.season-title {
  font-size: 20px;
  color: #233567;
}

.competition-title {
  font-size: 18px;
  color: #000000;
}

.competition-title:hover {
  background: #c4cad8c2;
}

.date {
  color: #a1a1a1 !important;
}

/* .search {
  background-color: #e8eeffc2;
  border: 0px;
  outline: none;
}

.serch:focus {
  background-color: #e8fcff50;
} */
</style>

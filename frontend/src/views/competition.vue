<template>
  <div style="height: 100%">
    <i-container class="_margin-bottom-1 _padding-bottom-1">
      <div id="title" class="_padding-top-1 _margin-bottom-1" style="text-align: center;">
        <a>{{ competition.title }}</a>
      </div>
      <div style="background-color: #e8eeffc2; border-radius: 20px;" class="_padding-1">
        <div v-for="(resultList, category) in competition.categoryList" :key="category">
          <div class="category-title _margin-bottom-1">{{ category }}</div>
          <div class="_margin-bottom-1">
          <i-table hover class="table">
            <thead>
              <tr>
                <th scope="row">#</th>
                <td>Атлет</td>
                <td>Страна</td>
                <td>Золото</td>
                <td>Серебро</td>
                <td>Бронза</td>
                <td>Общие баллы</td>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(result, index) in resultList" :key="index">
                <th scope="row">{{ index + 1 }}</th>
                <td>{{ result.sportsman }}</td>
                <td>{{ result.country }}</td>
                <td>{{ result.goldMedals }}</td>
                <td>{{ result.silverMedals }}</td>
                <td>{{ result.bronzeMedals }}</td>
                <td>{{ result.points }}</td>
              </tr>
            </tbody>
          </i-table>
          <!-- <i-container>
            <i-row>
              <i-column>{{ season.title }} {{ season.year }}</i-column>
            </i-row>
            <hr>
            <i-container>
              <i-list-group :bordered="false" style=" background-color: rgba(232, 238, 255, 0.76)">
                <i-list-group-item v-for="(competition, indcomp) in season.competitionList" :key="indcomp"
                  class="competition-title" @click="toCompetition(indseason, indcomp)" style="color: #233567;">
                  <a>{{ competition.title }}</a>
                    <a style="float:right" class="date">{{ competition.date }}</a>
                </i-list-group-item>
              </i-list-group>
            </i-container>
          </i-container> -->
        </div>
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

      competition: {} as any,
    };
  },
  methods: {
  },
  beforeMount() {
    const temp = this.$route.path.split('/')[2];
    if (temp !== undefined) {
      const [season, competition] = temp.split('.');
      this.competition = model.data.app.seasonList[parseInt(season)].competitionList[parseInt(competition)];
    } else {
      this.$router.replace(`/competition/0.0`);
      model.data.app.seasonList[0].competitionList[0];
    }
  }
});
</script>

<style scoped>
#title {
  color: #233567;
  font-size: 40px;
}

.category-title {
  color: #233567;
  font-size: 25px;
}
.table {
  border-radius: 10px !important;
}

.table td {
  background-color: #e8eeffc2 !important; 
}

.table th {
  background-color: #e8eeffc2 !important; 
}

</style>
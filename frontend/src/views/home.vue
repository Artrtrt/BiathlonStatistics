<template>
  <div style="height: 100%">
    <i-container class="_padding-bottom-1">
      <div
        style="
          float: right;
          padding-right: -30px;
          display: flex;
          grid-gap: 10px;
        "
        class="search"
      >
        <input
          @keydown.enter="search"
          ref="search-input"
          style="width: 300px"
          placeholder="Поиск по чемпионату"
        />
        <img @click="search" src="@/assets/magnifier.svg" class="button-icon" />
      </div>
      <div id="title" class="_padding-top-1 _margin-bottom-1">
        <a style="white-space: nowrap">Список сезонов </a>
        <a v-if="model.data.app.seasonList.length === 0">пуст</a>
      </div>
      <i-button
        v-if="isAdmin"
        @click="showSeasonAdd = true"
        class="button-confirm _margin-bottom-1"
        >Добавить сезон</i-button
      >
      <div
        v-if="model.data.app.seasonList.length !== 0"
        style="background-color: #e8eeffc2; border-radius: 10px"
        class="_padding-1"
      >
        <div v-if="!isMatch">
          <div class="_margin-bottom-1">Совпадений не найдено</div>
          <i-button @click="cancelSearch" class="button-confirm"
            >Отменить поиск</i-button
          >
        </div>
        <div
          v-for="(season, seasonIndex) in model.data.app.seasonList"
          :key="seasonIndex"
        >
          <div
            v-if="isMatchSeason[seasonIndex]"
            class="_margin-bottom-1 season-title _padding-1"
            style="background-color: #e8eeffc2; border-radius: 10px"
          >
            <i-container>
              <i-row style="align-items: center">
                <i-column
                  v-if="showСhangeSeason[seasonIndex]"
                  style="display: flex; flex-wrap: wrap; grid-gap: 10px"
                >
                  <i-input v-model="changedSeasonTitle"></i-input>
                  <i-input v-model="changedSeasonYear"></i-input>
                </i-column>
                <i-column class="_margin-left-1" v-else
                  >{{ season.title }} {{ season.year }}</i-column
                >
                <div
                  v-if="isAdmin"
                  style="
                    float: right;
                    display: flex;
                    flex-wrap: wrap;
                    grid-gap: 10px;
                  "
                >
                  <div
                    v-if="!showСhangeSeason[seasonIndex]"
                    class="button-icon"
                    @click="
                      showCompetitionAdd = true;
                      seasonInd = seasonIndex;
                    "
                  >
                    <img src="@/assets/plus.svg" />
                  </div>
                  <confirmationButton
                    @confirm="changeSeason(seasonIndex)"
                    @primary="
                      tempChangeSeason(season.title, season.year, seasonIndex)
                    "
                    @cancel="
                      showСhangeSeason[seasonIndex] = false;
                      changedSeasonTitle = '';
                      $forceUpdate();
                    "
                    :disabled="changedSeasonTitle !== ''"
                  >
                  </confirmationButton>
                  <div
                    @click="deleteSeason(seasonIndex)"
                    v-if="!showСhangeSeason[seasonIndex]"
                    class="button-icon"
                  >
                    <img src="@/assets/trash.svg" />
                  </div>
                </div>
              </i-row>
              <hr />
              <div
                v-for="(competition, compIndex) in season.competitionList"
                :key="compIndex"
              >
                <div v-if="competition.title.match(searchStr)">
                  <i-row style="align-items: center">
                    <i-column
                      v-if="showСhangeCompetition[seasonIndex][compIndex]"
                      style="display: flex; flex-wrap: wrap; grid-gap: 10px"
                    >
                      <i-input v-model="changedCompetitionTitle"></i-input>
                      <i-input v-model="changedCompetitionDate"></i-input>
                    </i-column>
                    <i-column v-else>
                      <div
                        class="competition-title"
                        @click="toCompetition(season.id, competition.id)"
                      >
                        <a>{{ competition.title }}</a>
                        <a style="float: right" class="date">
                          {{ competition.date }}</a
                        >
                      </div>
                    </i-column>
                    <div
                      v-if="isAdmin"
                      style="
                        float: right;
                        display: flex;
                        flex-wrap: wrap;
                        grid-gap: 10px;
                      "
                      class="_margin-left-1"
                    >
                      <confirmationButton
                        @confirm="changeCompetition(seasonIndex, compIndex)"
                        @primary="
                          tempChangeCompetition(
                            competition.title,
                            competition.date,
                            seasonIndex,
                            compIndex
                          )
                        "
                        @cancel="
                          showСhangeCompetition[seasonIndex][compIndex] = false;
                          changedCompetitionTitle = '';
                          $forceUpdate();
                        "
                        :disabled="changedCompetitionTitle !== ''"
                      >
                      </confirmationButton>
                      <div
                        v-if="!showСhangeCompetition[seasonIndex][compIndex]"
                        @click="deleteCompetition(seasonIndex, compIndex)"
                        class="button-icon"
                      >
                        <img src="@/assets/trash.svg" />
                      </div>
                    </div>
                  </i-row>
                  <hr
                    class="_margin-0"
                    v-if="compIndex !== season.competitionList.length - 1"
                    style="background-color: #f0f0f0c9"
                  />
                </div>
              </div>
            </i-container>
          </div>
        </div>
      </div>
    </i-container>

    <i-modal v-model="showSeasonAdd" @hide="cleanSeason">
      <template slot="header">
        <div class="text-header color-white header">Добавить сезон</div>
      </template>
      <i-container>
        <i-row class="_margin-bottom-1">
          <i-column xs="4" md="3" style="display: flex; align-items: center"
            >Название:</i-column
          >
          <i-column xs="8"><i-input v-model="seasonTitle"></i-input></i-column>
        </i-row>
        <i-row class="_margin-bottom-2">
          <i-column xs="4" md="3" style="display: flex; align-items: center"
            >Период:</i-column
          >
          <i-column xs="8"><i-input v-model="seasonYear"></i-input></i-column>
        </i-row>
        <div style="display: flex; justify-content: center">
          <i-button
            style="width: 130px"
            variant="primary"
            class="_margin-right-1 button-confirm"
            @click="addSeason"
            >Добавить</i-button
          >
          <i-button
            class="button-danger"
            @click="cleanSeason"
            style="width: 130px"
            >Отмена</i-button
          >
        </div>
      </i-container>
    </i-modal>

    <i-modal v-model="showCompetitionAdd" @hide="cleanCompetition">
      <template slot="header">
        <div class="text-header color-white">Добавить соревнование</div>
      </template>
      <i-container>
        <i-row class="_margin-bottom-1">
          <i-column xs="4" md="3" style="display: flex; align-items: center"
            >Название:</i-column
          >
          <i-column xs="8"
            ><i-input v-model="competitionTitle"></i-input
          ></i-column>
        </i-row>
        <i-row class="_margin-bottom-2">
          <i-column xs="4" md="3" style="display: flex; align-items: center"
            >Дата:</i-column
          >
          <i-column xs="8"
            ><i-input v-model="competitionDate"></i-input
          ></i-column>
        </i-row>
        <div style="display: flex; justify-content: center">
          <i-button
            style="width: 130px"
            variant="primary"
            class="_margin-right-1 button-confirm"
            @click="addCompetition"
            >Добавить</i-button
          >
          <i-button
            class="button-danger"
            @click="cleanCompetition"
            style="width: 130px"
            >Отмена</i-button
          >
        </div>
      </i-container>
    </i-modal>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";
import confirmationButton from "@/components/confirmationButton.vue";

export default Vue.extend({
  name: "HomePage",
  data() {
    return {
      model,

      isAdmin: model.data.auth.isAdmin,
      searchStr: "",
      isMatchSeason: [] as boolean[],
      isMatch: true,

      showSeasonAdd: false,
      seasonTitle: "",
      seasonYear: "",
      showСhangeSeason: [] as boolean[],
      changedSeasonTitle: "",
      changedSeasonYear: "",

      showCompetitionAdd: false,
      seasonInd: 0,
      competitionTitle: "",
      competitionDate: "",
      showСhangeCompetition: [[]] as boolean[][],
      changedCompetitionTitle: "",
      changedCompetitionDate: "",
    };
  },
  components: {
    confirmationButton,
  },
  methods: {
    toCompetition(season: number, competition: number) {
      this.$router.push(`/competition/${season}.${competition}`);
    },
    search() {
      const elem = this.$refs['search-input'] as HTMLInputElement; // eslint-disable-line
      this.searchStr = elem.value;
      let isMatchCompetition = false;
      model.data.app.seasonList.forEach((season, seasonIndex) => {
        season.competitionList.forEach((competition: any) => {
          if (competition.title.match(this.searchStr)) {
            isMatchCompetition = true;
            return;
          }
        });
        this.isMatchSeason[seasonIndex] = isMatchCompetition;
        isMatchCompetition = false;
      });
      this.isMatch = false;
      this.isMatchSeason.forEach((match) => {
        if (match) {
          this.isMatch = true;
        }
      });
      this.$forceUpdate();
    },
    cancelSearch() {
      this.searchStr = "";
      this.isMatchSeason.fill(true);
      this.isMatch = true;
      const elem = this.$refs['search-input'] as HTMLInputElement; // eslint-disable-line
      elem.value = "";
      this.$forceUpdate();
    },
    cleanSeason() {
      this.showSeasonAdd = false;
      this.seasonTitle = "";
      this.seasonYear = "";
    },
    async addSeason() {
      await model.method.app.addSeason(this.seasonTitle, this.seasonYear);
      this.cleanSeason();
      this.$forceUpdate();
    },
    tempChangeSeason(title: string, year: string, ind: number) {
      this.changedSeasonTitle = title;
      this.changedSeasonYear = year;
      this.showСhangeSeason[ind] = true;
      this.$forceUpdate();
    },
    async changeSeason(ind: number) {
      await model.method.app.updateSeason(
        ind,
        this.changedSeasonTitle,
        this.changedSeasonYear
      );
      this.showСhangeSeason[ind] = false;
      this.changedSeasonTitle = "";
      this.changedSeasonYear = "";
      this.$forceUpdate();
    },
    async deleteSeason(ind: number) {
      await model.method.app.deleteSeason(ind);
      this.$forceUpdate();
    },
    cleanCompetition() {
      this.showCompetitionAdd = false;
      this.competitionTitle = "";
      this.competitionDate = "";
    },
    async addCompetition() {
      await model.method.app.addCompetition(
        this.seasonInd,
        this.competitionTitle,
        this.competitionDate
      );
      this.cleanCompetition();
    },
    tempChangeCompetition(
      title: string,
      date: string,
      seasonInd: number,
      competitionInd: number
    ) {
      this.changedCompetitionTitle = title;
      this.changedCompetitionDate = date;
      this.showСhangeCompetition[seasonInd][competitionInd] = true;
      this.$forceUpdate();
    },
    async changeCompetition(seasonInd: number, compIndex: number) {
      await model.method.app.updateCompetition(
        seasonInd,
        compIndex,
        this.changedCompetitionTitle,
        this.changedCompetitionDate
      );
      this.showСhangeCompetition[seasonInd][compIndex] = false;
      this.changedCompetitionTitle = "";
      this.changedCompetitionDate = "";
      this.$forceUpdate();
    },
    async deleteCompetition(seasonInd: number, compInd: number) {
      await model.method.app.deleteCompetition(seasonInd, compInd);
      this.$forceUpdate();
    },
  },
  beforeMount() {
    model.data.app.seasonList.forEach((el, index) => {
      const length = el.competitionList.length;
      const filledCompetitionArray = Array(length).fill(false, 0, length);
      this.showСhangeCompetition[index] = filledCompetitionArray;
      this.showСhangeSeason.push(false);
      this.isMatchSeason.push(true);
    });
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
  padding: 15px;
  font-size: 18px;
  cursor: pointer;
  color: #233567;
}

.competition-title:hover {
  background: #c4cad8c2;
}

.date {
  color: #a1a1a1 !important;
}

.modal-bg {
  background-color: #c3d7ed;
}

.search {
  padding: 5px;
  background-color: #e8eeffc2;
  border-radius: 0px 0px 5px 5px;
}

.search input {
  background-color: #e8eeffc2;
  height: 30px;
  padding: 15px;
  border: 0px;
  outline: none;
}
</style>

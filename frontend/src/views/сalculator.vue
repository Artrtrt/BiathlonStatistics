<template>
  <div class="content-center">
    <i-card id="opacity-block">
      <template slot="header">
        <div class="text-header">
          <a style="color: #233567 !important; font-size: 20px;">Калькулятор</a>
        </div>
      </template>
      <i-layout>
      <i-layout vertical>
        <i-layout style="width: 60%" class="_margin-right-2">
          <i-layout-content>
          <i-row class="_margin-bottom-1">
            <i-column>
              <i-select v-model="seasonInd" placeholder="Выберите сезон">
                <i-select-option style="" v-for="(seasonUnit, index) in model.data.app.seasonList" :key="index"
                  :value="index.toString()" :label="`${seasonUnit.title} ${seasonUnit.year}`" />
              </i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-if="seasonInd !== ''">
            <i-column>
              <i-select v-model="competitionInd" placeholder="Выберите чемпионат">
                <i-select-option v-for="(competitionUnit, index) in model.data.app
                  .seasonList[parseInt(seasonInd)].competitionList" :key="index" :value="index.toString()"
                  :label="competitionUnit.title" />
              </i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-else>
            <i-column>
              <i-select :disabled="true" placeholder="Выберите чемпионат"></i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-if="competitionInd !== ''">
            <i-column>
              <i-select v-model="category" placeholder="Выберите категорию">
                <i-select-option v-for="(results, category) in model.data.app.seasonList[
                  parseInt(seasonInd)
                ].competitionList[parseInt(competitionInd)].categoryList" :key="category" :value="category"
                  :label="category" />
              </i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-else>
            <i-column>
              <i-select :disabled="true" placeholder="Выберите категорию"></i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-if="category !== ''">
            <i-column>
              <i-select v-model="country" placeholder="Выберите страну">
                <i-select-option v-for="(result, country) in countryList" :key="country" :value="country"
                  :label="country" />
              </i-select>
            </i-column>
          </i-row>
          <i-row class="_margin-bottom-1" v-else>
            <i-column>
              <i-select :disabled="true" placeholder="Выберите страну"></i-select>
            </i-column>
          </i-row>
        </i-layout-content>
        </i-layout>
        <i-layout style="width: 40%">
          <i-layout-header class="text-header _padding-top-0"><a>Результат</a></i-layout-header>
          <i-layout-content style="font-size: 16px">
            <i-container style="border: 1px solid">
              <i-row style="background-color: #f6fab4" class="_padding-bottom-1 _padding-top-1">
                <i-column xs="8" md="5" style="white-space: nowrap;">
                  <a>Золото:</a>
                </i-column>
                <i-column xs="3" style="white-space: nowrap;">
                  <a>{{ goldMedals }}</a>
                </i-column>
              </i-row>
              <i-row style="background-color: #e6e6e6" class="_padding-bottom-1 _padding-top-1">
                <i-column xs="8" md="5" style="white-space: nowrap;">
                  <a>Серебро:</a>
                </i-column>
                <i-column xs="3" style="white-space: nowrap;">
                  <a>{{ silverMedals }}</a>
                </i-column>
              </i-row>
              <i-row style="background-color: #e6c5a3" class="_padding-bottom-1 _padding-top-1">
                <i-column xs="8" md="5" style="white-space: nowrap;">
                  <a>Бронза:</a>
                </i-column>
                <i-column xs="3" style="white-space: nowrap;">
                  <a>{{ bronzeMedals }}</a>
                </i-column>
              </i-row>
            </i-container>
          </i-layout-content>
        </i-layout>
      </i-layout>
      <div style="background-color: rgba(232, 238, 255, 0.7) !important" class="_padding-left-0 _padding-bottom-0">
        <i-button style="width: 130px;" :disabled="disabledButton" variant="primary"
                class="_margin-right-1 button-confirm" @click="calc">Посчитать</i-button>
              <i-button  class="button-dunger" @click="clearData" style="width: 130px;">Стереть</i-button>
    </div>
    </i-layout>
    </i-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from "@/module/model";
import { ResultUnit } from "@/module/model/app";

export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,

      seasonInd: "",
      competitionInd: "",
      category: "",
      countryList: {} as { [country: string]: ResultUnit[] },
      country: "",

      goldMedals: "00",
      silverMedals: "00",
      bronzeMedals: "00",
    };
  },
  methods: {
    getCounryList() {
      const resultList =
        model.data.app.seasonList[parseInt(this.seasonInd)].competitionList[
          parseInt(this.competitionInd)
        ].categoryList[this.category];
      resultList.forEach((result) => {
        console.log(result);
        if (this.countryList[result.country]) {
          this.countryList[result.country].push(result);
        } else {
          this.countryList[result.country] = [result];
        }
      });
    },
    clearResult() {
      this.goldMedals = "00";
      this.silverMedals = "00";
      this.bronzeMedals = "00";
    },
    clearData() {
      this.seasonInd = "";
      this.competitionInd = "";
      this.category = "";
      this.countryList = {};
      this.country = "";
      this.clearResult();
    },
    calc() {
      let goldMedals = 0;
      let silverMedals = 0;
      let bronzeMedals = 0;
      this.countryList[this.country].forEach((result) => {
        goldMedals += result.goldMedals;
        silverMedals += result.silverMedals;
        bronzeMedals += result.bronzeMedals;
      });
      this.goldMedals = goldMedals.toString();
      this.silverMedals = silverMedals.toString();
      this.bronzeMedals = bronzeMedals.toString();
    },
  },
  computed: {
    disabledButton(): boolean {
      return (
        this.seasonInd === "" ||
        this.competitionInd === "" ||
        this.category === "" ||
        this.country === ""
      );
    },
  },
  watch: {
    seasonInd() {
      this.competitionInd = "";
      this.category = "";
      this.clearResult();
      this.countryList = {};
      this.country = "";
    },
    competitionInd() {
      this.category = "";
      this.clearResult();
      this.countryList = {};
      this.country = "";
    },
    category() {
      this.clearResult();
      this.country = "";
      this.getCounryList();
    },
    country() {
      this.clearResult();
    },
  },
});
</script>
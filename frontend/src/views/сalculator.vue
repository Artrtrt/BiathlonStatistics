<template>
  <div style="height: 100%">
    <i-container style="height: 100%; display: flex; align-items: center; justify-content: center;">
      <i-card style="width:500px; box-shadow: 5px 5px 30px black;">
        <template slot="header">Калькулятор</template>
        <i-layout vertical>
          <i-layout-aside class="_margin-right-2">
            <i-row class="_margin-bottom-1">
              <i-column>
                <i-select v-model="seasonInd" placeholder="Выберите сезон">
                  <i-select-option v-for="(seasonUnit, index) in model.data.app.seasonList" :key="index" :value="index.toString()" :label="`${seasonUnit.title} ${seasonUnit.year}`" />
                </i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-if="seasonInd !==''">
              <i-column>
                <i-select v-model="competitionInd" placeholder="Выберите чемпионат">
                  <i-select-option v-for="(competitionUnit, index) in model.data.app.seasonList[parseInt(seasonInd)].competitionList" :key="index" :value="index.toString()" :label="competitionUnit.title" />
                </i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-else>
              <i-column>
                <i-select :disabled="true" placeholder="Выберите чемпионат"></i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-if="competitionInd !==''">
              <i-column>
                <i-select v-model="category" placeholder="Выберите категорию">
                  <i-select-option v-for="(results, category) in model.data.app.seasonList[parseInt(seasonInd)].competitionList[parseInt(competitionInd)].categoryList" :key="category" :value="category" :label="category" />
                </i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-else>
              <i-column>
                <i-select :disabled="true" placeholder="Выберите категорию"></i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-if="category !==''">
              <i-column>
                <i-select v-model="country" placeholder="Выберите страну">
                  <i-select-option v-for="(result, country) in countryList" :key="country" :value="country" :label="country" />
                </i-select>
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1" v-else>
              <i-column>
                <i-select :disabled="true" placeholder="Выберите страну"></i-select>
              </i-column>
            </i-row>
            <i-row>
              <i-column>
                <i-button :disabled="disabledButton" variant="primary" class="_margin-right-1" @click="calc">Посчитать</i-button>
                <i-button variant="danger" @click="clearData">Стереть</i-button>
              </i-column>
            </i-row>
          </i-layout-aside>
          <i-layout>
            <i-layout-header>
            Результат
        </i-layout-header>
        <i-layout-content>
          <i-container style="border: 1px solid;">
            <i-row class="_margin-bottom-1 _margin-top-1">
              <i-column xs="7">
                Золото:
              </i-column>
              <i-column xs="3">
                {{ goldMedals }}
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1">
              <i-column xs="7">
                Серебро:
              </i-column>
              <i-column xs="3">
                {{ silverMedals }}
              </i-column>
            </i-row>
            <i-row class="_margin-bottom-1">
              <i-column xs="7">
                Бронза:
              </i-column>
              <i-column xs="3">
                {{ bronzeMedals }}
              </i-column>
            </i-row>
          </i-container>
        </i-layout-content>
      </i-layout>
        </i-layout>
      </i-card>
    </i-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import * as model from '@/module/model';
import { ResultUnit } from "@/module/model/app";

export default Vue.extend({
  name: "NetworkLan",
  data() {
    return {
      model,

      seasonInd: '',
      competitionInd: '',
      category: '',
      countryList: {} as {[country: string]: ResultUnit[]},
      country: '',
      
      goldMedals: '00',
      silverMedals: '00',
      bronzeMedals: '00',
    };
  },
  methods: {
    getCounryList() {
      console.log('aaa');
      const resultList = model.data.app.seasonList[parseInt(this.seasonInd)].competitionList[parseInt(this.competitionInd)].categoryList[this.category];
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
      this.goldMedals = '00';
      this.silverMedals = '00';
      this.bronzeMedals = '00';
    },
    clearData() {
      this.seasonInd = '';
      this.competitionInd = '';
      this.category = '';
      this.countryList = {};
      this.country = '';
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
      })
      this.goldMedals = goldMedals.toString();
      this.silverMedals = silverMedals.toString();
      this.bronzeMedals = bronzeMedals.toString();
    },
  },
  computed: {
    disabledButton(): boolean {
      return this.seasonInd ==='' || this.competitionInd ==='' || this.category ==='' || this.country === ''; 
    },
  },
  watch: {
    seasonInd() {
      this.competitionInd = '';
      this.category = '';
      this.clearResult();
      this.countryList = {};
      this.country = '';
    },
    competitionInd() {
      this.category = '';
      this.clearResult();
      this.countryList = {};
      this.country = '';
    },
    category() {
      this.clearResult();
      this.country = '';
      this.getCounryList();
    },
    country() {
      this.clearResult();
    },
  },
});
</script>

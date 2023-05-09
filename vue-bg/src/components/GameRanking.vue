<template>
  <div>
    <table class='ranking-table table-auto' v-if="!loadingCharacters">
      <thead>
        <tr>
          <th colspan="4"><h2>RANKING</h2></th>
        </tr>
      </thead>
      <thead>
        <tr>
          <th>Posició</th>
          <th>Usuari</th>
          <th>Nickname</th>
          <th>Nivell</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(character, index) in pageCharacters" :key="character.id">
          <td class="text-center flex justify-center items-center">
            <span v-if="((parseInt(this.currentPage) * this.charactersPerPage) - (this.charactersPerPage - index - 1)) >= 4">
              {{(parseInt(this.currentPage) * this.charactersPerPage) - (this.charactersPerPage - index - 1)}}
            </span>
            <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0" />
            </svg>
          </td>
          <td>{{ character.user__username }}</td>
          <td>{{ character.nickname }}</td>
          <td>{{ character.level }}</td>
        </tr>
      </tbody>
    </table>
    <nav class="pagination flex justify-center w-70">
      <ul class="list-style-none flex" v-if="!loadingCharacters">
        <li class="mx-1" @click="getPreviousPage()">
          <a class="relative block rounded-full bg-orange-300 px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200 dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </a>
        </li>
        <li class="mx-1" v-for="page in nPages()" :key="page" :aria-current="page == this.currentPage ? 'page' : false" @click="getRanking(page)">
          <a class="relative block rounded-full bg-orange-300 px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200  dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="" :class="{ 'bg-orange-400': (this.currentPage == page) }">{{ page }}
            <span v-if="page == this.currentPage" class="absolute -m-px h-px w-px overflow-hidden whitespace-nowrap border-0 p-0 [clip:rect(0,0,0,0)]">(current)</span>
          </a>
        </li>
        <li class="mx-1" @click="getNextPage()">
          <a class="relative block bg-orange-300 rounded-full px-3 py-1.5 text-sm text-neutral-600 transition-all duration-300 hover:bg-orange-200 dark:text-white dark:hover:bg-neutral-700 dark:hover:text-white"
            href="">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </a>
        </li>
      </ul>
      </nav>
  </div>
</template>

<script>
export default {
  name: 'RankingList',
  data() {
    const url = new URL(window.location.href);
    if (!url.searchParams.has('p') || !url.searchParams.has('c')){
      url.searchParams.append('p', 1);
      url.searchParams.append('c', 100);
    }
    window.history.replaceState({state: ''}, '', url);
    return {
      currentPage: url.searchParams.get('p'),
      charactersPerPage: url.searchParams.get('c'),
      characters: [],
      pageCharacters: [],
      loadingCharacters: true,
    }
  },
  methods: {
    nPages() {
      return Math.ceil(this.characters.length / this.charactersPerPage)
    },

    async getRanking(pageNumber = this.currentPage) {
      const url = new URL(window.location.href);
      url.searchParams.set('p', pageNumber);
      window.history.replaceState({state: ''}, '', url);
      let minCharacter = (pageNumber * this.charactersPerPage) - this.charactersPerPage
      let maxCharacter = (pageNumber * this.charactersPerPage)
      try {
        const response = await fetch(`/api/getRanking`);
        const data = await response.json();
        this.characters = data.characters;
        this.pageCharacters = this.characters.slice(minCharacter, Math.min(maxCharacter, this.characters.length))
        this.loadingCharacters = false;
      } catch (error) {
        console.error(error);
        this.loadingCharacters = false;
      }
    },

    getPreviousPage(){
      if(this.currentPage > 1){
        this.currentPage--;
        this.getRanking(this.currentPage);
      }
    },

    getNextPage(){
      if(this.currentPage < this.nPages()){
        this.currentPage++;
        this.getRanking(this.currentPage);
      }
    }
  },
  created() {
    this.getRanking()
  },
  watch: {
    charactersPerPage() {
      this.getRanking(this.currentPage)
    }
  }
}
</script>
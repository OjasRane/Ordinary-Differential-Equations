export type LanguageKeys = 'en'

type LanguageObject<T> = {
  [Lang in LanguageKeys]: T
}

export type LandingPageObj = {
  description: string
  getStartedBtnText: string
  githubBtnText: string
}

export const LANDING_PAGE: LanguageObject<LandingPageObj> = {
  en: {
    description: 'Explore the project: Ordinary Differential Equations',
    getStartedBtnText: 'Get started',
    githubBtnText: 'Source code',
  },
} as const

export const NAV: LanguageObject<{
  documentation: string
}> = {
  en: {
    documentation: 'Docs',
  },
} as const

export const ON_THIS_PAGE: LanguageObject<{
  onThisPage: string
  scrollToTop: string
}> = {
  en: {
    onThisPage: 'On this page',
    scrollToTop: 'Scroll to top',
  },
}

export const MISC: LanguageObject<{
  previous: string
  next: string
}> = {
  en: {
    next: 'Next',
    previous: 'Previous',
  },
}

export const SEARCH: LanguageObject<{
  search: string
  keepTyping: string
  noResults: string
  results: string
}> = {
  en: {
    search: 'Search',
    keepTyping: 'Keep typing...',
    noResults: 'No results',
    results: 'Results',
  },
}
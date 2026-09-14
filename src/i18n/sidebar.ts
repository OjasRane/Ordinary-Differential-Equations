import { type LanguageKeys } from '@/i18n/ui'

type SidebarSchema = {
  [Lang in LanguageKeys]: {
    introduction: string
    notebooks: string
    animations: string
    author: string
  }
}

export const SIDEBAR: SidebarSchema = {
  en: {
    introduction: 'Introduction',
    notebooks: 'Notebooks',
    animations: 'Animations',
    author: 'About the Author',
  },
}

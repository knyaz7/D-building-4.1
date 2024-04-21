import { ThemeProvider as ThemeProviderMUI } from "@mui/material"
import { FC, ReactNode } from "react"
import { themeConfig } from "./config"

interface Props {
  children: ReactNode
}

export const ThemeProvider: FC<Props> = ({ children }) => {
  return <ThemeProviderMUI theme={themeConfig}>{children}</ThemeProviderMUI>
}

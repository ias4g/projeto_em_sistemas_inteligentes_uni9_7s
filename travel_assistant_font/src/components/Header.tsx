import { AirplaneTiltIcon } from "@phosphor-icons/react";
import { COLORS } from '../constants';

export const Header = () => (
  <div className={`px-6 py-3 flex items-end justify-between border-b ${COLORS.BORDER}`}>
    <div className="flex flex-col items-center justify-center">
      <AirplaneTiltIcon className="size-10" style={{ color: COLORS.PRIMARY }} />
      <h1 className="text-2xl font-bold">
        <span style={{ color: COLORS.PRIMARY }}>travel</span>assistant
      </h1>
    </div>
    <div className="flex items-center gap-3">
      <span className="text-xs text-muted-foreground">
        Desenvolvido com ❤ como trabalho de conclusão do 7º semestre do curso de ciência da computação pela Universidade Nove de Julho
      </span>
    </div>
  </div>
); 
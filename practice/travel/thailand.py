class ThailandPackage:
    def detail(self):
        print("태국 여행 방콬 파타야 여행 50 만원")

if __name__ == "__main__":
    print("Thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thaildand 외부에서 모듈 호출 ")